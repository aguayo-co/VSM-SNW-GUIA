from django import template

from commons.models import DetailProductPage

register = template.Library()


@register.simple_tag(takes_context=True)
def get_grade_and_subject(context):
    catalog_items = {}
    list = DetailProductPage.objects.values_list("grade__name", "subject__name").distinct()
    for (key, value) in list:
        if key in catalog_items:
            catalog_items[key].append(value)
        else:
            catalog_items[key] = [value]
    context.update({"catalog_items": catalog_items,})
    return ""
