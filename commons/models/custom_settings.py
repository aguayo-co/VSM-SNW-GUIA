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

from .fields import SocialNetworksField
from wagtail_svg_images.models import ImageOrSvgField
from wagtail_svg_images.panels import ImageOrSVGPanel


@register_setting(icon="cogs")
class SantillanaSettings(BaseSetting):
    # Logos
    logo = ImageOrSvgField(
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
    logo_footer = ImageOrSvgField(
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

    # Contact
    phone = TextField(verbose_name=_("Teléfono"))
    email = EmailField(verbose_name=_("Email"))

    # Cookies
    cookies_text = RichTextField(
        verbose_name=_("Texto Cookies"), editor="inline", blank=True
    )

    # Scripts
    google_site_tag_script = TextField(verbose_name=_("Global site tag (gtag.js)"))
    google_tag_manager_script = TextField(verbose_name=_("Google Tag Manager"))
    google_tag_manager_no_script = TextField(
        verbose_name=_("Google Tag Manager (noscript)")
    )
    chatbot = TextField(verbose_name=_("Chatbot"), blank=True)

    # Panels
    panels = [
        MultiFieldPanel(
            [
                ImageOrSVGPanel("logo"),
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
                ImageOrSVGPanel("logo_footer"),
                FieldPanel("copyright"),
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
                FieldPanel("google_site_tag_script"),
                FieldPanel("google_tag_manager_script"),
                FieldPanel("google_tag_manager_no_script"),
                FieldPanel("chatbot"),
            ],
            heading=_("Scripts de terceros"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("cookies_text"),
            ],
            heading=_("Mensaje de Cookies"),
        ),
    ]

    class Meta:
        """Meta attributes for Settings."""

        verbose_name = _("Configuración Santillana")
        verbose_name_plural = _("Configuraciones Santillana")
