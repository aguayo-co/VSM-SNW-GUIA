from pydoc import locate


class FilterMixin:
    filter_form_class = "commons.forms.CatalogFilterForm"
    order_by_options = (
        ("grade", "Grado Ascendente"),
        ("-grade", "Grado Descendente"),
    )

    def get_filter_form(self, *args, **kwargs):
        request = kwargs.get("request", None)
        if request is not None:
            kwargs.pop("request")
        form_class = locate(self.filter_form_class)
        return form_class(*args, request.GET, **kwargs)