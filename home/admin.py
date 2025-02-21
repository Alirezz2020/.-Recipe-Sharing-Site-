from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'category')
    list_filter = ('created_at', 'author', 'category')
    search_fields = ('title', 'description', 'ingredients')
    filter_horizontal = ('tags',)  # easier selection for many-to-many field

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'author', 'rating', 'created_at')
    list_filter = ('created_at', 'rating', 'author')
    search_fields = ('text',)

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('user__username', 'recipe__title')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'read', 'created_at')
    list_filter = ('read', 'created_at', 'user')
    search_fields = ('user__username', 'message')



# class RecipeStepInline(admin.TabularInline):  # Allows adding steps within the Recipe admin
#     model = RecipeStep
#     extra = 1  # Provides an empty field for additional steps
#
#

