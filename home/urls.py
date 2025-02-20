from django.urls import path
from .views import (
    HomeView,
    RecipeDetailView,
    DashboardView,
    RecipeCreateView,
    RecipeUpdateView,
    RecipeDeleteView,
    CommentCreateView,
    ToggleFavoriteView,
    RecipeStepByStepView,
    NotificationListView,
    FavoriteListView,
)

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('favorites/', FavoriteListView.as_view(), name='favorites'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/<int:pk>/step/', RecipeStepByStepView.as_view(), name='recipe_step_by_step'),
    path('recipe/add/', RecipeCreateView.as_view(), name='recipe_add'),
    path('recipe/<int:pk>/edit/', RecipeUpdateView.as_view(), name='recipe_edit'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe_delete'),
    path('recipe/<int:pk>/comment/', CommentCreateView.as_view(), name='add_comment'),
    path('recipe/<int:pk>/favorite/', ToggleFavoriteView.as_view(), name='toggle_favorite'),
    path('notifications/', NotificationListView.as_view(), name='notifications'),
]
