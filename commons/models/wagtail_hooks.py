from django.utils.translation import gettext_lazy as _
from wagtail import hooks
from wagtail.contrib.modeladmin.options import modeladmin_register
from wagtail_tag_manager.wagtail_hooks import (
    ConstantModelAdmin,
    TagManagerAdminGroup,
    TagModelAdmin,
    TriggerModelAdmin,
    VariableModelAdmin,
)


@hooks.register("construct_settings_menu")
def hide_cookies_consent(request, menu_items):
    menu_items[:] = [
        item for item in menu_items if item.name != "cookie-consent-settings"
    ]


@hooks.register("construct_main_menu")
def hide_cookies_consent(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != "tag-manager"]


class CustomTagManagerAdminGroup(TagManagerAdminGroup):
    """Customized class for Tag Manager Group."""

    menu_label = _("Tag administrator")
    menu_icon = "code"
    menu_order = 640
    items = (
        TagModelAdmin,
        ConstantModelAdmin,
        VariableModelAdmin,
        TriggerModelAdmin,
    )


modeladmin_register(CustomTagManagerAdminGroup)
