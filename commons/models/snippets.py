from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class FooterMenuCategories(models.Model):
    """Footer column titles a.k.a footer menu categories."""

    name = models.CharField(max_length=255, verbose_name=_("Nombre"))

    panels = [
        FieldPanel("name"),
    ]

    def clean(self):
        """Validates the model instance."""
        model = self.__class__

    def __str__(self):
        """A readable representation."""
        return self.name

    class Meta:
        verbose_name = _("Categoría del menú footer")
        verbose_name_plural = _("Categorías del menú footer")