from django.utils.translation import gettext_lazy as _
from wagtail.core.blocks import (
    CharBlock,
    PageChooserBlock,
    RichTextBlock,
    StaticBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
    ListBlock,
    BooleanBlock,
)
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
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
            (
                "agregar_cifras",
                StructBlock(
                    [
                        ("icon", ImageChooserBlock(required=True, label=_("Icono"))),
                        ("value", CharBlock(required=False, label=_("Valor"))),
                        (
                            "description",
                            CharBlock(required=False, label=_("Descripción")),
                        ),
                    ]
                ),
            ),
        ],
        required=True,
        label=_("Lista de características"),
        min_num=1,
        max_num=3,
    )
    caption = (RichTextBlock(required=False, label=_("Leyenda"), editor="basic"),)
    primary_action_text = (CharBlock(required=False, label=_("Texto acción primaria")),)
    primary_action_url = (
        PageChooserBlock(required=False, label=_("URL acción primaria")),
    )

    class Meta:
        icon = "image"
        label = _("Social Proof")
        template = "commons/components/social_proof.html"


class CatalogIndexComponent(StructBlock):
    """
    A block that displays a catalog index.
    """

    title = CharBlock(required=True, label=_("Título"))
    subtitle = CharBlock(required=False, label=_("Sub título"))
    description = RichTextBlock(required=False, label=_("Descripción"), editor="inline")
    feature_list = StreamBlock(
        [
            (
                "bullet_line_text",
                CharBlock(required=False, label=_("Línea de texto bullet")),
            ),
            (
                "simple_line_text",
                CharBlock(required=False, label=_("Línea de texto simple")),
            ),
        ],
        required=False,
        label=_("Lista de características"),
    )
    caption = RichTextBlock(required=False, label=_("Leyenda"))
    primary_action_text = CharBlock(required=False, label=_("Texto acción primaria"))
    primary_action_url = PageChooserBlock(
        required=False, label=_("URL acción primaria")
    )
    catalog = StaticBlock(
        help_text=_(
            "Este componente incluye automaticamente todas las Series o Sellos Editoriales, "
            "así como el Indice de Grados > Materias"
        )
    )

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
            (
                "featured_content",
                StructBlock(
                    [
                        ("image", ImageChooserBlock(required=True, label=_("Imagen"))),
                        (
                            "description",
                            CharBlock(required=False, label=_("Descripción")),
                        ),
                        (
                            "primary_action_text",
                            CharBlock(required=False, label=_("Texto acción primaria")),
                        ),
                        (
                            "primary_action_url",
                            PageChooserBlock(
                                required=False, label=_("URL acción primaria")
                            ),
                        ),
                    ]
                ),
            ),
        ],
        required=True,
        label=_("Contenido destacado"),
        min_num=1,
        max_num=2,
    )

    class Meta:
        icon = "image"
        label = _("Featured Content")
        template = "commons/components/featured_content.html"


class TestimonialBlock(StructBlock):
    """A single testimonial block."""

    avatar = ImageChooserBlock(required=False, label=_("Imagen"))
    name_lastname = CharBlock(required=True, label=_("Nombre y apellido"))
    profession = CharBlock(required=False, label=_("Profesión"))
    review = TextBlock(required=True, label=_("Reseña"))


class TestimonialsComponent(StructBlock):
    """
    A block that displays testimonials.
    """

    title = CharBlock(required=False, label=_("Título"))
    add_testimonials = ListBlock(
        TestimonialBlock,
        required=False,
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

    title_featured = CharBlock(required=True, label=_("Título destacados"))
    subtitle_featured = CharBlock(required=True, label=_("Subtítulo destacados"))
    featured_link_list = ListBlock(
        PageChooserBlock(required=False, label=_("Enlace destacado")),
        required=False,
        label=_("Lista de enlaces destacados"),
        max_num=3,
    )
    title = CharBlock(required=False, label=_("Título"))
    subtitle = CharBlock(required=False, label=_("Subtítulo"))
    link_list = ListBlock(
        PageChooserBlock(
            page_type="commons.DetailArticlePage",
            required=True,
            label=_("Enlace"),
        ),
        required=False,
        label=_("Lista de enlaces"),
    )

    primary_action_text = CharBlock(required=False, label=_("Texto acción primaria"))
    primary_action_url = PageChooserBlock(
        page_type="commons.DetailArticlePage",
        required=True,
        label=_("URL acción primaria"),
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
    primary_action_url = PageChooserBlock(
        required=False, label=_("URL acción primaria")
    )
    secondary_action_text = CharBlock(
        required=False, label=_("Texto acción secundaria")
    )
    secondary_action_url = PageChooserBlock(
        required=False, label=_("URL acción secundaria")
    )
    background_illustration = ImageChooserBlock(
        required=False, label=_("Ilustración de fondo")
    )

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
    primary_action_url = PageChooserBlock(
        required=False, label=_("URL acción primaria")
    )
    secondary_action_text = CharBlock(
        required=False, label=_("Texto acción secundaria")
    )
    secondary_action_url = PageChooserBlock(
        required=False, label=_("URL acción secundaria")
    )

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
    primary_action_url = PageChooserBlock(
        required=False, label=_("URL acción primaria")
    )
    secondary_action_text = CharBlock(
        required=False, label=_("Texto acción secundaria")
    )
    secondary_action_url = PageChooserBlock(
        required=False, label=_("URL acción secundaria")
    )
    background_illustration = ImageChooserBlock(
        required=False, label=_("Ilustración de fondo")
    )

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


class DefinitionBlock(StructBlock):
    """A defintion is a small block with explanations."""

    title = CharBlock(required=True, label=_("Título"))
    content = RichTextBlock(required=True, label=_("Contenido"), editor="basic")


class DefinitionListComponent(StructBlock):
    """
    A block that displays a definition list.
    """

    title = CharBlock(required=True, label=_("Título"))
    subtitle = CharBlock(required=False, label=_("Subtítulo"))
    introduction = CharBlock(required=False, label=_("Introducción"))
    definition_list = ListBlock(
        DefinitionBlock,
        required=True,
        label=_("Definiciones"),
    )

    class Meta:
        icon = "list-ul"
        label = _("Lista de Definición")
        template = "commons/components/definition_list_component.html"


class BannerAdComponent(StructBlock):
    """
    A block that displays a banner ad.
    """

    banner_text = RichTextBlock(
        required=False, label=_("Texto de banner"), editor="basic"
    )
    link_text_scroll_to = CharBlock(
        required=False, label=_("Texto de enlace scroll to")
    )
    id_link_scroll_to = CharBlock(required=False, label=_("ID de enlace scroll to"))

    class Meta:
        icon = "image"
        label = _("Banner Ad")
        template = "commons/components/banner_ad_component.html"


class FreeContentComponent(StructBlock):
    """
    A block that displays a free content.
    """

    title = CharBlock(required=False, label=_("Título"))
    show_in_content_table = BooleanBlock(
        required=False, label=_("Mostrar en tabla de contenido")
    )
    content = StreamBlock(
        [
            (
                "rich_text",
                StructBlock(
                    [("rich_text", RichTextBlock())],
                    label=_("Texto Enriquecido"),
                    required=True,
                ),
            ),
            (
                "cite",
                StructBlock(
                    [
                        ("cite", RichTextBlock(required=True, label=_("Cita"))),
                        ("cite_author", CharBlock(required=False, label=_("Autor"))),
                        ("footnote", CharBlock(required=False, label=_("Nota"))),
                        ("url", PageChooserBlock(required=False, label=_("URL"))),
                    ],
                    label=_("Cita"),
                    required=False,
                ),
            ),
            (
                "image",
                StructBlock(
                    [
                        ("image", ImageChooserBlock(required=True, label=_("Imagen"))),
                        (
                            "description",
                            CharBlock(required=False, label=_("Descripción")),
                        ),
                        ("credits", CharBlock(required=False, label=_("Créditos"))),
                    ],
                    label=_("Imagen"),
                    required=False,
                ),
            ),
        ],
        label=_("Contenido"),
        required=True,
    )

    class Meta:
        icon = "image"
        label = _("Free Content")
        template = "commons/components/free_content_component.html"


class AgendaComponent(StructBlock):
    """
    A block that displays an agenda.
    """

    title = CharBlock(required=True, label=_("Título"))
    course_list = ListBlock(
        PageChooserBlock(required=False, label=_("Select páginas")),
        required=False,
        label=_("Listado de cursos"),
    )

    class Meta:
        icon = "list-ul"
        label = _("Agenda")
        template = "commons/components/agenda_component.html"


class ChipListComponent(StructBlock):
    """
    A block that displays an chip list.
    """

    title = CharBlock(required=True, label=_("Título"))
    link_list = ListBlock(
        PageChooserBlock(
            required=True,
            label=_("Enlace"),
        ),
        min_num=1,
        max_num=7,
        required=False,
        label=_("Lista de enlaces"),
    )
    primary_action_text = CharBlock(required=False, label=_("Texto acción primaria"))
    primary_action_url = PageChooserBlock(
        required=False,
        label=_("URL acción primaria"),
    )

    class Meta:
        icon = "list-ul"
        label = _("Listado de chips")
        template = "commons/components/chip_list_component.html"
