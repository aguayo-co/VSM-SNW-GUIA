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
from hitcount.models import HitCount
from hitcount.views import HitCountMixin


@hooks.register("before_serve_page")
def increment_view_count(page, request, serve_args, serve_kwargs):
    hit_count = HitCount.objects.get_for_object(page)
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    print(hit_count_response)
    print(hit_count.hits)


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

    menu_label = _("Etiqueta administrator")
    menu_icon = "code"
    menu_order = 640
    items = (
        TagModelAdmin,
        ConstantModelAdmin,
        VariableModelAdmin,
        TriggerModelAdmin,
    )


modeladmin_register(CustomTagManagerAdminGroup)
