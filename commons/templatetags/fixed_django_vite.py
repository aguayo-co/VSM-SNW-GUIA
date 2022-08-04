"""Module to override Django Vite Manifest loading."""
import json
from typing import Dict
from urllib.parse import urljoin

from django import template
from django.conf import settings
from django.core.files.storage import default_storage, get_storage_class
from django.utils.safestring import mark_safe
from django_vite.templatetags.django_vite import (
    DJANGO_VITE_DEV_MODE,
    DJANGO_VITE_MANIFEST_PATH,
    DJANGO_VITE_STATIC_URL,
    DjangoViteAssetLoader,
)

from vsm_snw.settings.base import BASE_DIR

register = template.Library()


class FixedDjangoViteAssetLoader(DjangoViteAssetLoader):
    def _parse_manifest(self) -> None:
        """
        Read and parse the Vite manifest file.
        Raises:
            RuntimeError: if cannot load the file or JSON in file is malformed.
        """
        vite_storage = get_storage_class(settings.STATICFILES_STORAGE)()
        try:
            manifest_file = vite_storage.open(str("manifest.json"), "r")
            manifest_content = manifest_file.read()
            manifest_file.close()
            self._manifest = json.loads(manifest_content)
        except Exception as error:
            raise RuntimeError(
                f"Error Parsing Vite Manifest (Aguayo) "
                f"{DJANGO_VITE_MANIFEST_PATH} : {str(error)}"
            )


@register.simple_tag
@mark_safe
def vite_asset(
    path: str,
    **kwargs: Dict[str, str],
) -> str:
    """
    Generates a <script> tag for this JS/TS asset and a <link> tag for
    all of its CSS dependencies by reading the manifest
    file (for production only).
    In development Vite loads all by itself.
    Arguments:
        path {str} -- Path to a Vite JS/TS asset to include.
    Returns:
        str -- All tags to import this file in your HTML page.
    Keyword Arguments:
        **kwargs {Dict[str, str]} -- Adds new attributes to generated
            script tags.
    Raises:
        RuntimeError: If cannot find the file path in the
            manifest (only in production).
    Returns:
        str -- The <script> tag and all <link> tags to import this
            asset in your page.
    """

    assert path is not None

    return FixedDjangoViteAssetLoader.instance().generate_vite_asset(path, **kwargs)

# Make Loader instance at startup to prevent threading problems
FixedDjangoViteAssetLoader.instance()