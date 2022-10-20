from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList
from django.utils.translation import gettext_lazy as _
from wagtail.blocks.struct_block import StructBlockValidationError, StructValue
from wagtail.core import blocks
from wagtail.core.blocks import (BooleanBlock, CharBlock, ListBlock,
                                 PageChooserBlock, RichTextBlock, StaticBlock,
                                 StreamBlock, StructBlock, TextBlock)
from wagtail.embeds.blocks import EmbedBlock
from wagtail_svg_images.blocks import ImageOrSVGBlock


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
                        (
                            "icon",
                            ImageOrSVGBlock("icon", required=False, label=_("Icono")),
                        ),
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
    primary_action_text = CharBlock(required=False, label=_("Texto acción primaria"))
    primary_action_url = PageChooserBlock(
        required=False, label=_("URL acción primaria")
    )
    caption = RichTextBlock(required=False, label=_("Leyenda"), editor="inline")

    def clean(self, value):
        result = super().clean(value)
        errors = {}
        if value["primary_action_text"] and not value["primary_action_url"]:
            errors["primary_action_url"] = ErrorList(
                [
                    _(
                        "Ha definido un Texto para el botón de acción primaria, por tanto debe seleccionar una pagina."
                    )
                ]
            )
        if errors:
            raise StructBlockValidationError(errors)
        return result

    class Meta:
        icon = "group"
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

    def clean(self, value):
        result = super().clean(value)
        errors = {}
        if value["primary_action_text"] and not value["primary_action_url"]:
            errors["primary_action_url"] = ErrorList(
                [
                    _(
                        "Ha definido un Texto para el botón de acción primaria, por tanto debe seleccionar una pagina."
                    )
                ]
            )
        if errors:
            raise StructBlockValidationError(errors)
        return result

    class Meta:
        icon = "grip"
        label = _("Índice de Catalogo")
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
                        (
                            "image",
                            ImageOrSVGBlock("image", required=True, label=_("Imagen")),
                        ),
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
        icon = "pick"
        label = _("Contenido destacado")
        template = "commons/components/featured_content.html"


class TestimonialBlock(StructBlock):
    """A single testimonial block."""

    avatar = ImageOrSVGBlock("avatar", required=False, label=_("Imagen"))
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
        icon = "view"
        label = _("Testimonios")
        template = "commons/components/testimonials.html"


class PagesLinksListComponent(StructBlock):
    """
    A block that displays a list of pages links.
    """

    title_featured = CharBlock(required=False, label=_("Título destacados"))
    subtitle_featured = CharBlock(required=False, label=_("Subtítulo destacados"))
    featured_link_list = ListBlock(
        PageChooserBlock(
            page_type="wagtailcore.Page",
            required=True,
            label=_("Enlace Destacado"),
        ),
        required=False,
        label=_("Lista de enlaces destacados"),
        max_num=3,
    )
    title_interest = CharBlock(required=False, label=_("Título enlaces de interés"))
    link_list = ListBlock(
        PageChooserBlock(
            page_type="commons.DetailArticlePage",
            required=True,
            label=_("Enlace"),
        ),
        required=False,
        label=_("Lista de enlaces"),
        max_num=6,
    )

    primary_action_text = CharBlock(required=False, label=_("Texto acción primaria"))
    primary_action_url = PageChooserBlock(
        page_type="commons.DetailArticlePage",
        required=False,
        label=_("URL acción primaria"),
    )

    def clean(self, value):
        result = super().clean(value)
        errors = {}
        if value["primary_action_text"] and not value["primary_action_url"]:
            errors["primary_action_url"] = ErrorList(
                [
                    _(
                        "Ha definido un Texto para el botón de acción primaria, por tanto debe seleccionar una pagina."
                    )
                ]
            )
        if errors:
            raise StructBlockValidationError(errors)
        return result

    class Meta:
        icon = "list-ul"
        label = _("Lista de enlaces de páginas")
        template = "commons/components/pages_links_list.html"


class SlideImageComponent(StructBlock):
    """
    A block that displays a slide image.
    """

    text_navigation = CharBlock(required=True, label=_("Texto de navegación"))
    title = CharBlock(required=True, label=_("Título"))
    subtitle = CharBlock(required=False, label=_("Subtítulo"))
    description = RichTextBlock(required=True, label=_("Descripción"), editor="list")
    image = ImageOrSVGBlock("image", required=True, label=_("Imagen"))
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
    background_illustration = ImageOrSVGBlock(
        "background_illustration", required=False, label=_("Ilustración de fondo")
    )

    def clean(self, value):
        result = super().clean(value)
        errors = {}
        if value["primary_action_text"] and not value["primary_action_url"]:
            errors["primary_action_url"] = ErrorList(
                [
                    _(
                        "Ha definido un Texto para el botón de acción primaria, por tanto debe seleccionar una pagina."
                    )
                ]
            )
        if value["secondary_action_text"] and not value["secondary_action_url"]:
            errors["secondary_action_url"] = ErrorList(
                [
                    _(
                        "Ha definido un Texto para el botón de acción secundaria, por tanto debe seleccionar una pagina."
                    )
                ]
            )
        if errors:
            raise StructBlockValidationError(errors)
        return result

    class Meta:
        icon = "image"
        label = _("Imagen del slide")
        template = "commons/components/slide_image.html"


class SlideImageBackgroundComponent(StructBlock):
    """
    A block that displays a slide image with a background.
    """

    text_navigation = CharBlock(required=True, label=_("Texto de navegación"))
    title = CharBlock(required=True, label=_("Título"))
    subtitle = CharBlock(required=False, label=_("Subtítulo"))
    description = RichTextBlock(required=True, label=_("Descripción"), editor="list")
    background_image = ImageOrSVGBlock(
        "background_image", required=True, label=_("Imagen")
    )
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

    def clean(self, value):
        result = super().clean(value)
        errors = {}
        if value["primary_action_text"] and not value["primary_action_url"]:
            errors["primary_action_url"] = ErrorList(
                [
                    _(
                        "Ha definido un Texto para el botón de acción primaria, por tanto debe seleccionar una pagina."
                    )
                ]
            )
        if value["secondary_action_text"] and not value["secondary_action_url"]:
            errors["secondary_action_url"] = ErrorList(
                [
                    _(
                        "Ha definido un Texto para el botón de acción secundaria, por tanto debe seleccionar una pagina."
                    )
                ]
            )
        if errors:
            raise StructBlockValidationError(errors)
        return result

    class Meta:
        icon = "image"
        label = _("Imagen de fondo")
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
    background_illustration = ImageOrSVGBlock(
        "background_illustration", required=False, label=_("Ilustración de fondo")
    )

    def clean(self, value):
        result = super().clean(value)
        errors = {}
        if value["primary_action_text"] and not value["primary_action_url"]:
            errors["primary_action_url"] = ErrorList(
                [
                    _(
                        "Ha definido un Texto para el botón de acción primaria, por tanto debe seleccionar una pagina."
                    )
                ]
            )
        if value["secondary_action_text"] and not value["secondary_action_url"]:
            errors["secondary_action_url"] = ErrorList(
                [
                    _(
                        "Ha definido un Texto para el botón de acción secundaria, por tanto debe seleccionar una pagina."
                    )
                ]
            )
        if errors:
            raise StructBlockValidationError(errors)
        return result

    class Meta:
        icon = "media"
        label = _("Video del slide")
        template = "commons/components/slide_video.html"


class ThematicContentItem(StructBlock):
    """sub bloque for add items of thematic content"""

    title = CharBlock(label=_("Título"), required=True)
    description = CharBlock(label=_("Descripción"), required=True)

    class Meta:
        """Propiedades del componente"""

        label = _("Items Contenidos Tematicos")
        icon = "radio-full"
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
                        (
                            "image",
                            ImageOrSVGBlock("image", required=True, label=_("Imagen")),
                        ),
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
            (
                "video",
                StructBlock(
                    [
                        ("video", EmbedBlock(required=True, label=_("Video"))),
                        (
                            "description",
                            CharBlock(required=False, label=_("Descripción")),
                        ),
                        ("credits", CharBlock(required=False, label=_("Créditos"))),
                    ],
                    label=_("Video"),
                    required=False,
                ),
            ),
        ],
        label=_("Contenido"),
        required=True,
    )

    class Meta:
        icon = "edit"
        label = _("Contenido Libre")
        template = "commons/components/free_content_component.html"


class AgendaComponent(StructBlock):
    """
    A block that displays an agenda.
    """

    title = CharBlock(required=True, label=_("Título"))
    subtitle = CharBlock(required=False, label=_("Subtítulo"))
    course_list = ListBlock(
        PageChooserBlock(required=False, label=_("Select páginas")),
        required=False,
        label=_("Listado de cursos"),
    )

    class Meta:
        icon = "date"
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

    def clean(self, value):
        result = super().clean(value)
        errors = {}
        if value["primary_action_text"] and not value["primary_action_url"]:
            errors["primary_action_url"] = ErrorList(
                [
                    _(
                        "Ha definido un Texto para el botón de acción primaria, por tanto debe seleccionar una pagina."
                    )
                ]
            )
        if errors:
            raise StructBlockValidationError(errors)
        return result

    class Meta:
        icon = "list-ul"
        label = _("Listado de chips")
        template = "commons/components/chip_list_component.html"


class ProductsListComponent(StructBlock):
    """
    A block that displays a products list.
    """

    title = CharBlock(required=True, label=_("Título"))
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
    products_list = ListBlock(
        PageChooserBlock(
            page_type="commons.DetailProductPage",
            required=True,
            label=_("Enlace a producto"),
        ),
        min_len=1,
        required=False,
        label=_("Listado de productos"),
    )

    def clean(self, value):
        result = super().clean(value)
        errors = {}
        if value["primary_action_text"] and not value["primary_action_url"]:
            errors["primary_action_url"] = ErrorList(
                [
                    _(
                        "Ha definido un Texto para el botón de acción primaria, por tanto debe seleccionar una pagina."
                    )
                ]
            )
        if value["secondary_action_text"] and not value["secondary_action_url"]:
            errors["secondary_action_url"] = ErrorList(
                [
                    _(
                        "Ha definido un Texto para el botón de acción secundaria, por tanto debe seleccionar una pagina."
                    )
                ]
            )
        if errors:
            raise StructBlockValidationError(errors)
        return result

    class Meta:
        icon = "list-ul"
        label = _("Listado de productos")
        template = "commons/components/products_list_component.html"


class NavigationIndexComponent(StructBlock):
    """
    A block that displays a navigation index.
    """

    info = StaticBlock(
        help_text=_(
            "Este componente muestra un indice de los componentes de esta página que hayan sido promovidos."
        ),
    )

    class Meta:
        icon = "list-ol"
        label = _("Índice de navegación")
        template = "commons/components/navigation_index_component.html"


# TODO @ramiro revisar este componente
class ContentHeroComponent(StructBlock):
    """
    A block that displays a content hero.
    """

    title = CharBlock(required=True, label=_("Título"))
    description = ListBlock(
        ThematicContentItem,
        required=False,
        label=_("Descripción"),
    )

    class Meta:
        icon = "image"
        label = _("Hero de contenido")
        template = "commons/components/content_hero_component.html"
