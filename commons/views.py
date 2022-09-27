from django.views.generic import TemplateView


class Test404View(TemplateView):
    template_name = "404.html"


class Test500View(TemplateView):
    template_name = "500.html"
