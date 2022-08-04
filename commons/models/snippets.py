from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class Degree(models.Model):
    """Degree tag for books (products)."""

    name = models.CharField(max_length=255, verbose_name=_("Nombre"))
    number = models.IntegerField(verbose_name=_("Número"))

    panels = [
        FieldPanel("name"),
        FieldPanel("number"),
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

    name = models.CharField(max_length=255, verbose_name=_("Nombre"), null=True, blank=True)
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
        FieldPanel("image"),
    ]

    def __str__(self):
        """A readable representation."""
        return self.name

    class Meta:
        verbose_name = _("Serie")
        verbose_name_plural = _("Series")