from django import template

register = template.Library()


@register.filter
def multiply(value, arg):
    """Multiplica o value pelo arg."""
    try:
        return value * arg
    except (ValueError, TypeError):
        return ""
