from django.urls import path
from private.views import DashboardPageView, MyLoginView

urlpatterns = [
    path('dashboard/', DashboardPageView.as_view(), name='dashboard'),
    path("login/", MyLoginView.as_view(), name="user_login"),
]