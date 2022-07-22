from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class Degree(models.Model):
    """Degree tag for books (products)."""

    name = models.CharField(max_length=255, verbose_name=_("Nombre"))

    panels = [
        FieldPanel("name"),
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