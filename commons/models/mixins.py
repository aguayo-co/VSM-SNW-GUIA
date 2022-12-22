from pydoc import locate

from django.utils.translation import gettext_lazy as _


class FilterMixin:
    filter_form_class = "commons.forms.CatalogFilterForm"
    search_filter_form_class = "commons.forms.SearchForm"
    filter_names = ["serie", "subject", "grade"]

    def get_filter_form(self, *args, **kwargs):
        request = kwargs.get("request", None)
        if request is not None:
            kwargs.pop("request")
        form_class = locate(self.filter_form_class)
        return form_class(*args, request.GET, **kwargs)

    def get_search_filter_form(self, *args, **kwargs):
        request = kwargs.get("request", None)
        if request is not None:
            kwargs.pop("request")
        search_form_class = locate(self.search_filter_form_class)
        return search_form_class(*args, request.GET, **kwargs)


class OrderMixin:
    order_by_options = (
        ("relevance", _("Los más relevantes")),
        ("-visits", _("Los más populares")),
        ("title", _("Ordenar A/Z")),
        ("-title", _("Ordenar Z/A")),
    )

    def get_order_by(self, request):
        order_by = request.GET.get("order_by", None)
        return order_by if order_by in [x[0] for x in self.order_by_options] else None

    def get_order_by_options(self):
        return self.order_by_options
