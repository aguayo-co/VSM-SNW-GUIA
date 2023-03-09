from django.urls import reverse
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from vsm_snw.settings.base import WAGTAIL_FRONTEND_LOGIN_TEMPLATE


class MyLoginView(LoginView):
    template_name = WAGTAIL_FRONTEND_LOGIN_TEMPLATE


class DashboardPageView(LoginRequiredMixin, TemplateView):
    template_name = "private/dashboard.html"
