from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Recipe

# Public Home view – all recipes ordered by newest first
class HomeView(ListView):
    model = Recipe
    template_name = 'home/home.html'
    context_object_name = 'recipes'
    paginate_by = 6
    ordering = ['-created_at']  # Correct field name


# Recipe detail view
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
    fields = ['title', 'description', 'ingredients', 'instructions', 'image']
    success_url = reverse_lazy('home:dashboard')  # or another URL of your choice

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update recipe view – only allow if user is the recipe's author
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    template_name = 'home/recipe_form.html'
    fields = ['title', 'description', 'ingredients', 'instructions', 'image']

    def test_func(self):
        recipe = self.get_object()
        return recipe.author == self.request.user

# Delete recipe view – only allow if user is the recipe's author
class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = 'home/recipe_confirm_delete.html'
    success_url = reverse_lazy('home:dashboard')

    def test_func(self):
        recipe = self.get_object()
        return recipe.author == self.request.user
