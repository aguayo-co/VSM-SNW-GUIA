from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtailmenus.models import (
    AbstractFlatMenuItem,
    AbstractMainMenu,
    AbstractMainMenuItem,
    FlatMenuItem,
)


class AGFlatMenuItem(AbstractFlatMenuItem):
    """A custom menu item model to be used by ``wagtailmenus.MainMenu``"""

    menu = ParentalKey(
        "wagtailmenus.FlatMenu",
        on_delete=models.CASCADE,
        related_name="custom_flat_menu_items",
    )
