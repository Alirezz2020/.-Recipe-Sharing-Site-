from django import template

register = template.Library()

@register.filter
def is_favorited_by(recipe, user):
    if not user.is_authenticated:
        return False
    return recipe.favorited_by.filter(user=user).exists()
