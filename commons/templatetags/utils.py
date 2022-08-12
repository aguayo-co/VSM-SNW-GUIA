from django import template

register = template.Library()


@register.filter
def next(a_list, current_position):
    """Retorna el siguiente elemento de una lista a partir de la posición actual (0-Based)."""
    try:
        return a_list[int(current_position) + 1]
    except IndexError:
        return None


@register.filter
def prev(a_list, current_position):
    """Retorna el anterior elemento de una lista a partir de la posición actual (0-Based)."""
    if int(current_position) == 0:
        return None
    try:
        return a_list[int(current_position) - 1]
    except IndexError:
        return None
