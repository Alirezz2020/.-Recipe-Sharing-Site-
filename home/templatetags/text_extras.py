from django import template

register = template.Library()

@register.filter
def splitlines(value):
    """
    Splits the given text into a list of lines.
    Usage: {{ some_text|splitlines }}
    """
    if isinstance(value, str):
        return value.splitlines()
    return []
