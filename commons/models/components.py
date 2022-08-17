from django.utils.translation import gettext_lazy as _
from wagtail.core.blocks import (
    BooleanBlock,
    CharBlock,
    PageChooserBlock,
    RichTextBlock,
    StaticBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
    ListBlock,
)
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.models import Image
from wagtail.core import blocks


class SocialProofComponent(StructBlock):
    """
    A block that displays a social proof.
    """

    title = CharBlock(required=True, label=_("Título"))
    subtitle = CharBlock(required=False, label=_("Sub título"))
    introduction = CharBlock(required=False, label=_("Introducción"))
    add_figures = StreamBlock(
        [
            ("agregar_cifras", StructBlock([
                ("icon", ImageChooserBlock(required=True, label=_("Icono"))),
                ("value", CharBlock(required=True, label=_("Valor"))),
                ("description", CharBlock(required=False, label=_("Descripción"))),
            ])),
        ],
        required = True,
        label = _("Lista de características"),
        min_num = 1,
        max_num = 3,
    )
    caption = RichTextBlock(required=False, label=_("Leyenda"), editor="basic"),
    primary_action_text = CharBlock(required=False, label=_("Texto acción primaria")),
    primary_action_url = PageChooserBlock(required=False, label=_("URL acción primaria")),

    class Meta:
        icon = "image"
        label = _("Social Proof")
        template = "commons/components/social_proof.html"


class CatalogIndexComponent(StructBlock):
    """
    A block that displays a catalog index.
    """

    title = CharBlock(required=True, label=_("Título"))
    description = RichTextBlock(required=False, label=_("Descripción"), editor="inline")
    feature_list = StreamBlock(
        [
            ("bullet_line_text", CharBlock(required=False, label=_("Línea de texto bullet"))),
            ("simple_line_text", CharBlock(required=False, label=_("Línea de texto simple"))),
        ],
        required = False,
        label=_("Lista de características"),
    )
    caption = RichTextBlock(required=False, label=_("Leyenda")),
    degree_subject_snippet = StaticBlock(
        required=False, label=_("Snippet de grado de estudios")
    )
    subtitle = CharBlock(required=False, label=_("Sub título"))
    # How to use StatikBlocks in this case?
    series = StaticBlock(required=False, label=_("Serie"))
    primary_action_text = CharBlock(required=False, label=_("Texto acción primaria")),
    primary_action_url = PageChooserBlock(required=False, label=_("URL acción primaria")),

    class Meta:
        icon = "image"
        label = _("Catalogo Index")
        template = "commons/components/catalog_index.html"


class FeaturedContentComponent(StructBlock):
    """
    A block that displays a featured content.
    """

    title = CharBlock(required=True, label=_("Título"))
    subtitle = CharBlock(required=False, label=_("Subtítulo"))
    description = RichTextBlock(required=True, label=_("Descripción"), editor="basic")
    add_featured_content = StreamBlock(
        [
            ("featured_content", StructBlock([
                ("image", ImageChooserBlock(required=True, label=_("Imagen"))),
                ("description", CharBlock(required=False, label=_("Descripción"))),
                ("primary_action_text", CharBlock(required=False, label=_("Texto acción primaria"))),
                ("primary_action_url", PageChooserBlock(required=False, label=_("URL acción primaria"))),
            ])),
        ],
        required = True,
        label=_("Contenido destacado"),
        min_num = 1,
        max_num = 2,
    )

    class Meta:
        icon = "image"
        label = _("Featured Content")
        template = "commons/components/featured_content.html"


class TestimonialsComponent(StructBlock):
    """
    A block that displays testimonials.
    """
    title = CharBlock(required=False, label=_("Título"))
    add_testimonials = StreamBlock(
        [
            ("testimonial", StructBlock([
                ("avatar", ImageChooserBlock(required=False, label=_("Imagen"))),
                ("name_lastname", CharBlock(required=True, label=_("Nombre y apellido"))),
                ("profession", CharBlock(required=False, label=_("Profesión"))),
                ("review", TextBlock(required=True, label=_("Reseña"))),
            ])),
        ],
        required = False,
        label=_("Testimonios"),
    )

    class Meta:
        icon = "image"
        label = _("Testimonials")
        template = "commons/components/testimonials.html"


class PagesLinksListComponent(StructBlock):
    """
    A block that displays a list of pages links.
    """
    title = CharBlock(required=True, label=_("Título"))
    subtitle = CharBlock(required=True, label=_("Subtítulo"), editor="inline")
    featured_link_list = ListBlock(
        PageChooserBlock(required=False, label=_("Enlace destacado")),
        required=False,
        label=_("Lista de enlaces destacados"),
        max_num=3,
    )
    link_list = ListBlock(
        StructBlock([
            ("title", CharBlock(required=False, label=_("Título"))),
            ("subtitle", RichTextBlock(required=False, label=_("Subtítulo"), editor="inline")),
            ("primary_action_text", CharBlock(required=False, label=_("Texto acción primaria"))),
            ("primary_action_url", PageChooserBlock(required=False, label=_("URL acción primaria"))),
        ]),
        required=False,
        label=_("Lista de enlaces"),
    )

    class Meta:
        icon = "image"
        label = _("Pages Links List")
        template = "commons/components/pages_links_list.html"


class SlideImageComponent(StructBlock):
    """
    A block that displays a slide image.
    """
    text_navigation = CharBlock(required=True, label=_("Texto de navegación"))
    title = CharBlock(required=True, label=_("Título"))
    subtitle = CharBlock(required=False, label=_("Subtítulo"))
    description = RichTextBlock(required=True, label=_("Descripción"), editor="list")
    image = ImageChooserBlock(required=True, label=_("Imagen"))
    primary_action_text = CharBlock(required=False, label=_("Texto acción primaria"))
    primary_action_url = PageChooserBlock(required=False, label=_("URL acción primaria"))
    secondary_action_text = CharBlock(required=False, label=_("Texto acción secundaria"))
    secondary_action_url = PageChooserBlock(required=False, label=_("URL acción secundaria"))
    background_illustration = ImageChooserBlock(required=False, label=_("Ilustración de fondo"))

    class Meta:
        icon = "image"
        label = _("Slide Image")
        template = "commons/components/slide_image.html"


class SlideImageBackgroundComponent(StructBlock):
    """
    A block that displays a slide image with a background.
    """
    text_navigation = CharBlock(required=True, label=_("Texto de navegación"))
    title = CharBlock(required=True, label=_("Título"))
    subtitle = CharBlock(required=False, label=_("Subtítulo"))
    description = RichTextBlock(required=True, label=_("Descripción"), editor="list")
    background_image = ImageChooserBlock(required=True, label=_("Imagen"))
    primary_action_text = CharBlock(required=False, label=_("Texto acción primaria"))
    primary_action_url = PageChooserBlock(required=False, label=_("URL acción primaria"))
    secondary_action_text = CharBlock(required=False, label=_("Texto acción secundaria"))
    secondary_action_url = PageChooserBlock(required=False, label=_("URL acción secundaria"))

    class Meta:
        icon = "image"
        label = _("Slide Image Background")
        template = "commons/components/slide_image_background.html"


class SlideVideoComponent(StructBlock):
    """
    A block that displays a slide video.
    """
    text_navigation = CharBlock(required=True, label=_("Texto de navegación"))
    title = CharBlock(required=True, label=_("Título"))
    subtitle = CharBlock(required=False, label=_("Subtítulo"))
    description = RichTextBlock(required=True, label=_("Descripción"), editor="list")
    video = EmbedBlock(required=True, label=_("Video Url"))
    primary_action_text = CharBlock(required=False, label=_("Texto acción primaria"))
    primary_action_url = PageChooserBlock(required=False, label=_("URL acción primaria"))
    secondary_action_text = CharBlock(required=False, label=_("Texto acción secundaria"))
    secondary_action_url = PageChooserBlock(required=False, label=_("URL acción secundaria"))
    background_illustration = ImageChooserBlock(required=False, label=_("Ilustración de fondo"))

    class Meta:
        icon = "image"
        label = _("Slide Video")
        template = "commons/components/slide_video.html"


class ThematicContentItem(StructBlock):
    """sub bloque for add items of thematic content"""

    title = CharBlock(label=_("Título"), required=True)
    description = CharBlock(label=_("Descripción"), required=True)

    class Meta:
        """Propiedades del componente"""
        label = _("Items Contenidos Tematicos")
        icon = "list-ul"
        template = "components/thematic_content_item.html"


class ThematicContentComponent(StructBlock):
    """Component for add items of thematic content"""

    title = CharBlock(label=_("Título"), required=True)
    items = blocks.ListBlock(ThematicContentItem, label=_("Items"))

    class Meta:
        """Propiedades del componente"""
        label = _("Contenidos Tematicos")
        icon = "list-ul"
        template = "components/thematic_content.html"


class DefinitionListComponent(StructBlock):
    """
    A block that displays a definition list.
    """
    title = CharBlock(required=True, label=_("Título"))
    subtitle = CharBlock(required=False, label=_("Subtítulo"))
    introduction = CharBlock(required=False, label=_("Introducción"))
    definition_list = ListBlock(
        StructBlock([
            ("title", CharBlock(required=True, label=_("Título"))),
            ("content", RichTextBlock(required=True, label=_("Contenido"), editor="basic")),
        ]),
        required=True,
        label=_("Lista de definiciones"),
    )

    class Meta:
        icon = "list-ul"
        label = _("Definition List")
        template = "commons/components/definition_list_component.html"
