"""Centro de Ayuda templatetags."""
from django import template
from django.template.loader import render_to_string

from commons.forms import SearchForm

register = template.Library()


@register.simple_tag(takes_context=False)
def get_search_form(form=None):
    """Retorna el formulario de búsqueda."""
    if form is None:
        form = SearchForm()
    return form
