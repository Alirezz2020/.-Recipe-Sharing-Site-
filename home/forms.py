from django import forms
from django.forms import inlineformset_factory
from .models import *

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'image']

StepFormSet = inlineformset_factory(
    Recipe, Step,
    fields=('order', 'description'),

    extra=1,  # Number of extra forms
    can_delete=True
)