from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import InlinePanel
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractForm,
    AbstractFormField,
)

from commons.models import BasePage, FullStreamField


class FormField(AbstractFormField):
    page = ParentalKey("FormPage", on_delete=models.CASCADE, related_name="form_fields")


class FormPage(AbstractForm):
    CONTENT_FIELD = "_content_form"

    _content_form = FullStreamField(verbose_name=("Contenido"), null=True, blank=True)

    content_panels = AbstractForm.content_panels + [
        InlinePanel("form_fields", label=_("Campos del Formulario")),
    ]

    class Meta:
        verbose_name = _("Formulario")
        verbose_name_plural = _("Formularios")
