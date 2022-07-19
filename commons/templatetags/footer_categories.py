from django import template

from commons.models import FooterMenuCategories

register = template.Library()


@register.simple_tag(takes_context=True)
def get_footer_menu_categories(context):
    context.update({"categories": FooterMenuCategories.objects.all()})
    return ""
