from collections import defaultdict

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


@register.simple_tag(takes_context=True)
def get_hero_control_text(context):
    elements = defaultdict(lambda: {"prev": None, "next": None})
    for index, block in enumerate(context["self"].hero):
        # Prev Element
        if index != 0:
            elements[index + 1]["prev"] = (
                context["self"].hero[index - 1].value["text_navigation"]
            )

        # Next Element
        try:
            elements[index + 1]["next"] = (
                context["self"].hero[index + 1].value["text_navigation"]
            )
        except IndexError:
            pass
    return elements
