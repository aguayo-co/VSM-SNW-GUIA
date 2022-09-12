from django import template

from commons.models import DetailProductPage, Serie, CatalogPage

register = template.Library()


@register.simple_tag(takes_context=True)
def get_index(context):
    page_content = context.get("page").content
    index = []
    for block in page_content:
        if "free_content_component" == block.block_type and block.value["show_in_content_table"] is True:
            index.append(block)
    context.update({"index": index})
    return ""