from django.forms import BooleanField
from django.forms.widgets import CheckboxInput
from django.db import models
from django.utils.translation import gettext_lazy as _
from commons.models.fields import DetailProductIntroStreamField
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import InlinePanel, FieldPanel
from wagtail.contrib.forms.forms import FormBuilder
from wagtail.core.models import Site
from wagtail.contrib.forms.models import (
    AbstractForm,
    AbstractFormField,
    FORM_FIELD_CHOICES,
)

from commons.models.custom_settings import SantillanaSettings


class TermsAndConditionsCheckboxInput(CheckboxInput):
    """Custom input widget for terms and conditions field."""
    pass


class CaptchaCheckboxInput(CheckboxInput):
    """Custom input widget for captcha field."""
    pass


class FormField(AbstractFormField):
    CHOICES = (
        FORM_FIELD_CHOICES
        + (("terms_and_conditions", _("Términos y condiciones")),)
        + (("captcha", _("Captcha")),)
    )
    page = ParentalKey("FormPage", related_name="form_fields")
    field_type = models.CharField(
        verbose_name="field type", max_length=32, choices=CHOICES
    )


class CustomFormBuilder(FormBuilder):
    def create_terms_and_conditions_field(self, field, options):
        return BooleanField(
            label=SantillanaSettings.for_site(
                Site.objects.first()
            ).terms_and_conditions,
            required=field.required,
            widget=TermsAndConditionsCheckboxInput,
        )

    def create_captcha_field(self, field, options):
        return BooleanField(
            label=_("¿Eres humano?"),
            required=field.required,
            widget=CaptchaCheckboxInput,
        )


class FormPage(AbstractForm):
    form_builder = CustomFormBuilder

    CONTENT_FIELD = "_content_form"

    _content_form = DetailProductIntroStreamField(
        verbose_name=("Intro"), null=True, blank=True)

    content_panels = AbstractForm.content_panels + [
        FieldPanel(CONTENT_FIELD),
        InlinePanel("form_fields", label=_("Campos del Formulario")),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["key_recaptcha"] = SantillanaSettings.for_site(
            Site.objects.first()
        ).key_recaptcha
        return context

    @classmethod
    def replace_content_field(cls, field_name):
        """Replace content field in admin and `content` property interface."""
        content_panels = []
        for panel in cls.content_panels:
            if panel.field_name != cls.CONTENT_FIELD:
                content_panels.append(panel)
                continue
            content_panels.append(FieldPanel(field_name))

        return content_panels

    @property
    def content(self):
        """Devuelve el campo de contenido definido en CONTENT_FIELD."""
        return getattr(self, self.CONTENT_FIELD)

    class Meta:
        verbose_name = _("Formulario")
        verbose_name_plural = _("Formularios")
