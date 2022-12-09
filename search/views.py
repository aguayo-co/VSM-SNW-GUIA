from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse
from django.views.generic import ListView
from wagtail.models import Page
from wagtail.search.models import Query

from commons.models import BasePage, DetailProductPage, FilterMixin
from commons.models.mixins import OrderMixin


def search(request):
    search_query = request.GET.get("query", None)
    page = request.GET.get("page", 1)

    # Search
    if search_query:
        search_results = Page.objects.live().specific().search(search_query)
        query = Query.get(search_query)

        # Record hit
        query.add_hit()
    else:
        search_results = Page.objects.none()

    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return TemplateResponse(
        request,
        "search/search_list.html",
        {
            "search_query": search_query,
            "search_results": search_results,
        },
    )


class SearchView(FilterMixin, ListView, OrderMixin):
    template_name = "search/search_list.html"
    queryset = BasePage.objects.live().specific()
    paginate_by = 10
    filter_form_class = "commons.forms.CatalogFilterForm"
    search_filter_form_class = "commons.forms.SearchForm"

    def get_queryset(self):
        search_query = self.request.GET.get("query", None)
        queryset = super().get_queryset()
        order_by = self.get_order_by(self.request)

        # Exclude Redirections
        queryset.exclude(
            content_type__model__in=["externalredirect", "homepage", "thankyoupage"]
        )

        # Allow Relevance Order
        if order_by == "relevance":
            order_by = None

        # Filter
        if self.request.GET.get("type", None) == "catalog":
            queryset = DetailProductPage.objects.live()

        # Ordering
        if order_by:
            queryset = queryset.order_by(order_by)

        # Search
        queryset = queryset.search(search_query, order_by_relevance=False)

        return queryset

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update(
            {
                "filter_form": self.get_filter_form(
                    *args, request=self.request, **kwargs
                ),
                "search_filter_form": self.get_search_filter_form(
                    *args, request=self.request, **kwargs
                ),
                "order_by_options": self.get_order_by_options(),
            }
        )
        return context
