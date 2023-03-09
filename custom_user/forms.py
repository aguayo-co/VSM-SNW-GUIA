from django import forms
from django.utils.translation import gettext_lazy as _
from wagtail.users.forms import UserEditForm, UserCreationForm


class CustomUserEditForm(UserEditForm):
    name_school = forms.CharField(required=False, label=_("Nombre de la escuela"))
    work_center_key = forms.CharField(required=False, label=_("Clave del Centro de Trabajo"))
    grade_attends = forms.CharField(required=False, label=_("Grado que atiende"))
    federal_entity = forms.CharField(required=False, label=_("Entidad Federativa"))
    phone = forms.CharField(required=False, label=_("Teléfono"))


class CustomUserCreationForm(UserCreationForm):
    name_school = forms.CharField(required=False, label=_("Nombre de la escuela"))
    work_center_key = forms.CharField(required=False, label=_("Clave del Centro de Trabajo"))
    grade_attends = forms.CharField(required=False, label=_("Grado que atiende"))
    federal_entity = forms.CharField(required=False, label=_("Entidad Federativa"))
    phone = forms.CharField(required=False, label=_("Teléfono"))
