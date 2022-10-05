from collections import defaultdict

from django import template

from commons.models import DetailProductPage, Serie, CatalogPage

register = template.Library()


@register.simple_tag(takes_context=True)
def get_catalog_index(context):
    catalog_items = defaultdict(list)
    element_list = DetailProductPage.objects.distinct().order_by("grade__number")
    for product in element_list:
        catalog_items[product.grade].append(product.subject)
    catalog_items = {key: sorted(set(values), key = lambda x: x.name) for key, values in catalog_items.items()}
    context.update({"catalog_items": catalog_items})
    return ""


@register.simple_tag(takes_context=True)
def get_series(context):
    context.update({"series": Serie.objects.iterator()})
    return ""


@register.simple_tag(takes_context=True)
def get_catalog_page(context):
    context.update({"catalog_page": CatalogPage.objects.live().first()})
    print(context)
    return ""
