from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from wagtail import hooks
from wagtail.contrib.modeladmin.options import modeladmin_register
from wagtail_tag_manager.wagtail_hooks import (
    ConstantModelAdmin,
    TagManagerAdminGroup,
    TagModelAdmin,
    TriggerModelAdmin,
    VariableModelAdmin,
)


@hooks.register("before_serve_page")
def increment_view_count(page, request, serve_args, serve_kwargs):
    hit_count = HitCount.objects.get_for_object(page)
    HitCountMixin.hit_count(request, hit_count)


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


# @hooks.register("before_serve_page")
# def process_redirection(page, request, serve_args, serve_kwargs):
#     """Prevents redirections to be served and inmediatelly redirects to external URL."""
#     from commons.models import ExternalRedirect
#
#     if isinstance(page, ExternalRedirect):
#         return HttpResponseRedirect(page.redirect_url)
