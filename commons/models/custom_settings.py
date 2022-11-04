from django.db import models
from django.db.models import (
    PROTECT,
    SET_NULL,
    ForeignKey,
    TextField,
    EmailField,
)
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel

from .fields import SocialNetworksField


@register_setting(icon="cogs")
class SantillanaSettings(BaseSetting):
    # Logos
    logo = ForeignKey(
        "wagtailimages.Image",
        verbose_name=_("Logo del sitio"),
        on_delete=PROTECT,
        related_name="+",
        null=True,
    )
    logo_url = ForeignKey(
        "wagtailcore.Page",
        verbose_name=_("URL Logo"),
        on_delete=PROTECT,
        related_name="+",
        null=True,
    )

    # Social Networks
    social_networks = SocialNetworksField(_("Redes sociales"), blank=True, default=dict)

    # Footer
    logo_footer = ForeignKey(
        "wagtailimages.Image",
        verbose_name=_("Logo del footer"),
        on_delete=SET_NULL,
        null=True,
        related_name="+",
        help_text=_(
            "Logo alternativo que se utiliza en lugares de contraste oscuro, como el footer."
        ),
    )
    copyright = RichTextField(verbose_name=_("Copyright - Footer "), editor="inline")
    contact_page = ForeignKey(
        "forms.FormPage",
        verbose_name=_("Página de contacto"),
        on_delete=PROTECT,
        related_name="+",
        null=True,
    )

    # Contact
    phone = TextField(verbose_name=_("Teléfono"))
    email = EmailField(verbose_name=_("Email"))

    # Cookies
    cookies_text = RichTextField(
        verbose_name=_("Texto Cookies"), editor="inline", blank=True
    )

    # Terms and Conditions
    terms_and_conditions = RichTextField(
        verbose_name=_("Términos y condiciones"),
        editor="inline",
        blank=True,
    )

    # key recaptcha
    key_recaptcha = TextField(
        verbose_name=_("Key reCAPTCHA"),
        null=True,
        blank=True,
    )

    # secret recaptcha
    secret_recaptcha = TextField(
        verbose_name=_("Secret reCAPTCHA"),
        null=True,
        blank=True,
    )

    # Panels
    panels = [
        MultiFieldPanel(
            [
                ImageChooserPanel("logo"),
                FieldPanel("logo_url"),
            ],
            heading=_("Logo Principal"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("social_networks"),
            ],
            heading=_("Redes sociales"),
        ),
        MultiFieldPanel(
            [
                ImageChooserPanel("logo_footer"),
                FieldPanel("copyright"),
                FieldPanel("contact_page"),
            ],
            heading=_("Footer"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("phone"),
                FieldPanel("email"),
            ],
            heading=_("Contacto"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("cookies_text"),
            ],
            heading=_("Mensaje de Cookies"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("terms_and_conditions"),
                FieldPanel("key_recaptcha"),
            ],
            heading=_("Configuraciones de formularios"),
        ),
    ]

    class Meta:
        """Meta attributes for Settings."""

        verbose_name = _("Configuración Santillana")
        verbose_name_plural = _("Configuraciones Santillana")
