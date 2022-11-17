from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.documents import get_document_model
from wagtail.snippets.models import register_snippet
from wagtail.images.edit_handlers import ImageChooserPanel


@register_snippet
class Degree(models.Model):
    """Degree tag for books (products)."""

    name = models.CharField(max_length=255, verbose_name=_("Nombre"))
    number = models.IntegerField(verbose_name=_("Número"))
    color = models.CharField(
        max_length=255,
        verbose_name=_("Color"),
        choices=(
            ("turquesa", _("Turquesa")),
            ("yellow", _("Amarillo")),
            ("blue", _("Azul")),
        ),
        default="turquesa",
        help_text=_("Personaliza la apariencia del Grado cambiando el color"),
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Imagen"),
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("number"),
        FieldPanel("color"),
        ImageChooserPanel("image"),
    ]

    def __str__(self):
        """A readable representation."""
        return self.name

    class Meta:
        verbose_name = _("Grado")
        verbose_name_plural = _("Grados")


@register_snippet
class Subject(models.Model):
    """Subject tag for books (products)."""

    name = models.CharField(max_length=255, verbose_name=_("Nombre"))

    panels = [
        FieldPanel("name"),
    ]

    def __str__(self):
        """A readable representation."""
        return self.name

    class Meta:
        verbose_name = _("Materia")
        verbose_name_plural = _("Materias")


@register_snippet
class Serie(models.Model):
    """Serie tag."""

    name = models.CharField(
        max_length=255, verbose_name=_("Nombre"), null=True, blank=True
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Imagen"),
    )
    type = models.CharField(
        max_length=255,
        choices=(("serie", _("Serie")), ("editorial", _("Editorial"))),
        verbose_name=_("Tipo"),
        default="serie",
    )

    panels = [
        FieldPanel("name"),
        ImageChooserPanel("image"),
        FieldPanel("type"),
    ]

    def __str__(self):
        """A readable representation."""
        return self.name

    class Meta:
        verbose_name = _("Serie")
        verbose_name_plural = _("Series")


@register_snippet
class Book(models.Model):
    """Book (product) model."""

    name = models.CharField(max_length=255, verbose_name=_("Nombre"))
    external_link = models.ForeignKey(
        "commons.ExternalRedirect",
        verbose_name=_("Libro externo"),
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )
    document = models.ForeignKey(
        "wagtaildocs.Document",
        verbose_name=_("Documento"),
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )

    panels = [
        FieldPanel("name"),
        PageChooserPanel("external_link"),
        FieldPanel("document"),
    ]

    def __str__(self):
        """A readable representation."""
        return self.name

    def clean(self):
        """Validate that either external_link or document are set and there is only one of the two options."""
        if (not self.external_link and not self.document) or (
            self.external_link and self.document
        ):
            raise ValidationError(
                _(
                    "No puede utilizar ambos recursos ni dejar vacíos estos campos, por favor utilice solo una de las \
                dos opciones: Enlace Externo o Documento."
                )
            )

    class Meta:
        verbose_name = _("Libro")
        verbose_name_plural = _("Libros")
