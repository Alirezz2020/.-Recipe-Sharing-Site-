from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse

from .forms import *
from .models import Recipe, Comment, Favorite, Notification

# Public Home view with advanced search/filtering (ordered by newest first)
class HomeView(ListView):
    model = Recipe
    template_name = 'home/home.html'
    context_object_name = 'recipes'
    paginate_by = 6
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        category = self.request.GET.get('category')
        tag = self.request.GET.get('tag')
        if q:
            queryset = queryset.filter(title__icontains=q)
        if category:
            queryset = queryset.filter(category__name__iexact=category)
        if tag:
            queryset = queryset.filter(tags__name__iexact=tag)
        return queryset.distinct()

# Recipe detail view with social sharing and nutritional info
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'home/recipe_detail.html'

# Dashboard view – list of current user's recipes
class DashboardView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'home/dashboard.html'
    context_object_name = 'recipes'
    paginate_by = 6
    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user).order_by('-created_at')

# Create new recipe view – author is set automatically
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'home/recipe_form.html'
    fields = ['title', 'description', 'ingredients', 'image', 'category', 'tags', 'nutritional_info']

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['steps'] = StepFormSet(self.request.POST)
        else:
            data['steps'] = StepFormSet()
        return data

    def form_valid(self, form):
        form.instance.author = self.request.user
        context = self.get_context_data()
        steps = context['steps']
        if steps.is_valid():
            self.object = form.save()
            steps.instance = self.object
            steps.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    template_name = 'home/recipe_form.html'
    fields = ['title', 'description', 'ingredients', 'image', 'category', 'tags', 'nutritional_info']
    success_url = reverse_lazy('home:dashboard')

    def get_success_url(self):
        return reverse('home:dashboard')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['steps'] = StepFormSet(self.request.POST, instance=self.object)
        else:
            data['steps'] = StepFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        steps = context['steps']



        if steps.is_valid():
            form.instance.author = self.request.user
            self.object = form.save()
            steps.instance = self.object
            steps.save()
            return HttpResponseRedirect(self.get_success_url())  # Force redirect
        else:

            return self.render_to_response(self.get_context_data(form=form))

    def test_func(self):
        return self.get_object().author == self.request.user

# Delete recipe view – only allow if user is the recipe's author
class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = 'home/recipe_confirm_delete.html'
    success_url = reverse_lazy('home:dashboard')
    def test_func(self):
        return self.get_object().author == self.request.user

# Comment creation view – for adding comments/reviews to a recipe
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text', 'rating']
    template_name = 'home/comment_form.html'
    def form_valid(self, form):
        recipe = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        form.instance.recipe = recipe
        form.instance.author = self.request.user
        response = super().form_valid(form)
        # Create a notification for the recipe author if commenter is not the author
        if recipe.author != self.request.user:
            Notification.objects.create(
                user=recipe.author,
                message=f"{self.request.user.username} commented on your recipe {recipe.title}",
                url=reverse('home:recipe_detail', kwargs={'pk': recipe.pk})
            )
        return response
    def get_success_url(self):
        return reverse('home:recipe_detail', kwargs={'pk': self.kwargs['pk']})

# Toggle Favorite view – adds or removes a recipe from the user's favorites
class ToggleFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        favorite, created = Favorite.objects.get_or_create(user=request.user, recipe=recipe)
        if not created:
            favorite.delete()
        return redirect(request.META.get('HTTP_REFERER', 'home:home'))

# Step-by-Step Mode view for interactive recipe instructions

class RecipeStepByStepView(DetailView):
    """
    Displays the recipe in a step-by-step manner.
    Iterates over the related Step objects for the recipe.
    """
    model = Recipe
    template_name = 'home/recipe_step_by_step.html'


# Notifications list view
class NotificationListView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'home/notifications.html'
    context_object_name = 'notifications'
    paginate_by = 10
    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user).order_by('-created_at')

# Favorites list view
class FavoriteListView(LoginRequiredMixin, ListView):
    model = Favorite
    template_name = 'home/favorites.html'
    context_object_name = 'favorites'
    paginate_by = 6
    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user).order_by('-created_at')
