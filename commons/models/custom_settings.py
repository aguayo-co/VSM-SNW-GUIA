from django.db import models
from django.db.models import (
    PROTECT,
    SET_NULL,
    ForeignKey,
    TextField,
)
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.fields import RichTextField

from .fields import SocialNetworksField


@register_setting(icon="cogs")
class SantillanaSettings(BaseSetting):
    # Logos
    logo = ForeignKey(
        "wagtailimages.Image",
        verbose_name=_("Logo del sitio"),
        on_delete=PROTECT,
        related_name="+",
        blank=True,
        null=True,
    )
    logo_url = ForeignKey(
        "wagtailcore.Page",
        verbose_name=_("URL Logo"),
        on_delete=PROTECT,
        related_name="+",
        blank=True,
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
        blank=True,
        related_name="+",
        help_text=_(
            "Logo alternativo que se utiliza en lugares de contraste oscuro, como el footer."
        ),
    )
    copyright = RichTextField(verbose_name=_("Copyright - Footer "), editor="inline")

    # Contact
    phone = RichTextField(verbose_name=_("Teléfono"), editor="inline")
    email = RichTextField(verbose_name=_("Email"))

    # Cookies
    cookies_text = RichTextField(
        verbose_name=_("Texto Cookies"),
        editor="inline",
    )

    # Scripts
    google_site_tag_script = TextField(verbose_name=_("Global site tag (gtag.js)"))
    google_tag_manager_script = TextField(verbose_name=_("Google Tag Manager"))
    google_tag_manager_no_script = TextField(
        verbose_name=_("Google Tag Manager (noscript)")
    )

    # Panels
    panels = [
        MultiFieldPanel(
            [
                FieldPanel("logo"),
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
                FieldPanel("logo_footer"),
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
            ],
            heading=_("Scripts de terceros"),
        ),
    ]

    @property
    def allies(self):
        """Returns a list of allies."""
        return Ally.objects.all()

    class Meta:
        """Meta attributes for Settings."""

        verbose_name = "Configuración Santillana"
        verbose_name_plural = "Configuraciones Santillana"
