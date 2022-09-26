from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from django.db.models import CharField, ForeignKey, TextField, URLField
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.admin.panels import ObjectList, StreamFieldPanel, TabbedInterface
from wagtail.core.models import Page
from wagtail.core.templatetags.wagtailcore_tags import pageurl
from wagtail.documents import get_document_model_string
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail_svg_images.models import ImageOrSvgField
from wagtail_svg_images.panels import ImageOrSVGPanel
from hitcount.models import HitCountMixin

from commons.models.components import ThematicContentComponent
from commons.models.fields import (
    CategoryHomePageStreamField,
    ContentPageStreamField,
    CatalogPageStreamField,
    CourseDetailStreamField,
    DetailProductIntroStreamField,
    DetailProductStreamField,
    FullStreamField,
    HeroStreamField,
    HomeStreamField,
    ThematicHomePageStreamField,
)
from commons.models.mixins import FilterMixin, OrderMixin
from commons.models.snippets import Degree

items_per_page = 10


class BasePage(Page, HitCountMixin):
    """The basic model that all Pages inherit from."""

    CONTENT_FIELD = "_content_base"

    _content_base = FullStreamField(verbose_name=("Contenido"), null=True, blank=True)

    search_image = ImageOrSvgField(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Imagen para buscadores."),
    )
    keywords = models.CharField(
        default="", blank=True, max_length=100, verbose_name=_("Palabras clave")
    )

    is_creatable = False

    content_panels = Page.content_panels + [FieldPanel(CONTENT_FIELD)]
    promote_panels = [
        MultiFieldPanel(
            [
                FieldPanel("seo_title"),
                FieldPanel("search_description"),
                ImageOrSVGPanel("search_image"),
            ],
            heading=_("SEO"),
        ),
        FieldPanel("slug"),
        MultiFieldPanel(
            [
                FieldPanel("show_in_menus"),
            ],
            heading=_("Menús"),
        ),
    ]
    settings_panels = Page.settings_panels + []

    subpage_types = [
        "commons.BlogPage",
        "commons.ContentPage",
        "forms.FormPage",
        "commons.HomePage",
    ]

    @classmethod
    def replace_content_field(cls, field_name):
        """Replace content field in admin and `content` property interface."""
        content_panels = []
        for panel in cls.content_panels:
            if panel.field_name != cls.CONTENT_FIELD:
                content_panels.append(panel)
                continue
            content_panels.append(FieldPanel(field_name))

        return content_panels

    def clean(self):
        """adds `content` validation."""
        super().clean()

        # Slug Accents
        self.slug = slugify(self.slug)

    @classmethod
    def can_create_at(cls, parent):
        return (
            hasattr(parent.specific, "subpage_types")
            and cls in parent.specific.subpage_types
            or super().can_create_at(parent)
        )

    @property
    def content(self):
        """Devuelve el campo de contenido definido en CONTENT_FIELD."""
        return getattr(self, self.CONTENT_FIELD)

    class Meta:
        verbose_name = _("Página Base")
        verbose_name_plural = _("Páginas Base")


class HomePage(BasePage):
    """Home page model."""

    CONTENT_FIELD = "_content_home"

    _content_home = HomeStreamField(verbose_name=_("Contenido"), null=True, blank=True)

    hero = HeroStreamField()

    content_panels = [
        FieldPanel("title"),
        FieldPanel("hero"),
        FieldPanel(CONTENT_FIELD),
    ]
    subpage_types = [
        "commons.BlogPage",
        "commons.CatalogPage",
        "commons.ContentPage",
        "forms.FormPage",
        "commons.ExternalRedirect",
    ]

    class Meta:
        verbose_name = _("Home")
        verbose_name_plural = _("Home")


class BlogPage(BasePage, OrderMixin):
    """Model for the blog page."""

    CONTENT_FIELD = "_content_blog"

    _content_blog = StreamField([], verbose_name=_("Contenido"), null=True, blank=True)

    content_panels = BasePage.replace_content_field(CONTENT_FIELD)

    subpage_types = [
        "commons.CategoryHomePage",
        "commons.ThematicHomePage",
    ]

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blog")

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        page = request.GET.get("page", None)
        order_by = self.get_order_by(request)
        if order_by:
            queryset = CategoryHomePage.objects.all().order_by(order_by)
        else:
            queryset = CategoryHomePage.objects.all()

        paginator = Paginator(queryset, 1)

        try:
            frequent_questions = paginator.page(page)
        except PageNotAnInteger:
            frequent_questions = paginator.page(1)
        except EmptyPage:
            frequent_questions = paginator.page(paginator.num_pages)

        context["sub_pages"] = frequent_questions
        context["order_by"] = order_by
        context["order_by_options"] = self.get_order_by_options()

        return context


class CatalogPage(FilterMixin, BasePage, OrderMixin):
    """Catalog page model."""

    CONTENT_FIELD = "_content_catalog"

    _content_catalog = CatalogPageStreamField(
        verbose_name=_("Contenido"),
        null=True,
        blank=True
    )

    content_panels = BasePage.replace_content_field(CONTENT_FIELD)
    subpage_types = [
        "commons.DetailProductPage",
    ]

    class Meta:
        verbose_name = _("Catálogo")
        verbose_name_plural = _("Catálogo")

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        page = request.GET.get("page", None)
        order_by = self.get_order_by(request)

        # filters
        filter_names = ["serie", "subject", "grade"]
        filters = {
            f"{a_filter}__in": request.GET.getlist(a_filter, None)
            for a_filter in filter_names
            if request.GET.get(a_filter, None) not in ["", None]
        }
        if order_by:
            queryset = DetailProductPage.objects.filter(**filters).order_by(order_by)
        else:
            queryset = DetailProductPage.objects.filter(**filters)
        paginator = Paginator(queryset, items_per_page)

        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        context["object_list"] = object_list
        context["filter_form"] = self.get_filter_form(*args, request=request, **kwargs)
        context["order_by"] = order_by
        context["order_by_options"] = self.get_order_by_options()

        return context


class ContentPage(BasePage):
    """Model for the content page."""

    CONTENT_FIELD = "_content_content"

    _content_content = DetailProductIntroStreamField(
        verbose_name=("Intro"), null=True, blank=True
    )

    footer_content = ContentPageStreamField(
        verbose_name=("Contenido"), null=True, blank=True
    )

    content_panels = [
        FieldPanel(CONTENT_FIELD),
        FieldPanel("footer_content"),
    ]

    subpage_types = []

    class Meta:
        verbose_name = _("Contenido")
        verbose_name_plural = _("Contenidos")


class CourseDetailPage(BasePage):
    """Model for the course detail page."""

    CONTENT_FIELD = "_content_course_detail"

    _content_course_detail = DetailProductIntroStreamField(
        verbose_name=("Intro"), null=True, blank=True
    )

    footer_content = CourseDetailStreamField(
        verbose_name=("Contenido"), null=True, blank=True
    )

    hero = HeroStreamField(null=True, blank=True)

    responsible = CharField(
        verbose_name=_("Responsable"),
        max_length=255,
        null=True,
        blank=True,
    )
    date_time_event = models.DateTimeField(
        verbose_name=_("Fecha y hora del evento"),
        null=True,
        blank=True,
    )
    hashtag_youtube = CharField(
        verbose_name=_("Hashtag Youtube"),
        max_length=255,
        null=True,
        blank=True,
    )
    registration_form_url = models.URLField(
        verbose_name=_("Url Formulario de Inscripción"),
        null=True,
        blank=True,
    )

    content_panels = [
        FieldPanel("title"),
        FieldPanel("hero"),
        FieldPanel(CONTENT_FIELD),
        FieldPanel("footer_content"),
    ]
    promote_panels = BasePage.promote_panels
    settings_panels = BasePage.settings_panels
    course_information = [
        MultiFieldPanel(
            [
                FieldPanel("responsible"),
                FieldPanel("date_time_event"),
                FieldPanel("hashtag_youtube"),
                FieldPanel("registration_form_url"),
            ],
            heading=_("Información del Curso"),
        ),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading=_("Contenido")),
            ObjectList(promote_panels, heading=_("Promocionar")),
            ObjectList(settings_panels, heading=_("Propiedades"), classname="settings"),
            ObjectList(course_information, heading=_("Información del Curso")),
        ]
    )

    class Meta:
        verbose_name = _("Detalle de Curso")
        verbose_name_plural = _("Detalle de Cursos")


class CategoryHomePage(BasePage, OrderMixin):
    """Model for the category commons page."""

    CONTENT_FIELD = "_content_category_homepage"

    _content_category_homepage = CategoryHomePageStreamField(
        verbose_name=_("Contenido"), null=True, blank=True
    )

    content_panels = BasePage.replace_content_field(CONTENT_FIELD)

    subpage_types = [
        "commons.DetailArticlePage",
        "commons.CourseDetailPage",
    ]

    class Meta:
        verbose_name = _("Home de categoría")
        verbose_name_plural = _("Home de categorías")

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        page = request.GET.get("page", None)
        order_by = self.get_order_by(request)
        if order_by:
            queryset = DetailArticlePage.objects.all().order_by(order_by)
        else:
            queryset = DetailArticlePage.objects.all()

        paginator = Paginator(queryset, items_per_page)

        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        context["object_list"] = object_list
        context["order_by"] = order_by
        context["order_by_options"] = self.get_order_by_options()

        return context


class ThematicHomePage(BasePage, OrderMixin):
    """Model for the thematic commons page."""

    CONTENT_FIELD = "_content_thematic_homepage"

    _content_thematic_homepage = ThematicHomePageStreamField(
        verbose_name=("Contenido"), null=True, blank=True
    )

    content_panels = BasePage.replace_content_field(CONTENT_FIELD)

    subpage_types = [
        "commons.CourseDetailPage",
    ]

    class Meta:
        verbose_name = _("Home de temática")
        verbose_name_plural = _("Home de temáticas")

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        page = request.GET.get("page", None)
        order_by = self.get_order_by(request)
        if order_by:
            queryset = CourseDetailPage.objects.child_of(self).live().order_by(order_by)
        else:
            queryset = CourseDetailPage.objects.child_of(self).live()

        paginator = Paginator(queryset, items_per_page)

        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        context["object_list"] = object_list
        context["order_by"] = order_by
        context["order_by_options"] = self.get_order_by_options()

        return context


class DetailProductPage(BasePage):
    """Model for the detail product page."""

    IDIOM_CHOICES = [
        ("en", _("Inglés")),
        ("es", _("Español")),
    ]

    CONTENT_FIELD = "_content_detail_product"

    intro_detail_product = DetailProductIntroStreamField(
        verbose_name=_("Características y Beneficios"), null=True, blank=True
    )
    _content_detail_product = DetailProductStreamField(
        verbose_name=_("Contenido"), null=True, blank=True
    )
    thematic_content = StreamField(
        block_types=[
            ("thematic_content", ThematicContentComponent()),
        ],
        verbose_name=_("Contenidos Temáticos"),
        null=True,
        blank=True,
    )
    short_description = TextField(
        verbose_name=_("Descripción Corta"),
        null=True,
        blank=True,
    )
    image = ImageOrSvgField(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Imagen del Libro"),
    )
    grade = models.ForeignKey(
        "commons.Degree",
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Grado"),
        null=True,
        blank=True,
    )
    subject = models.ForeignKey(
        "commons.Subject",
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Asignatura"),
        null=True,
        blank=True,
    )
    serie = models.ForeignKey(
        "commons.Serie",
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Serie o Editorial"),
        null=True,
        blank=True,
    )
    campo_formacion = CharField(
        verbose_name=_("Campo formación"),
        max_length=255,
        null=True,
        blank=True,
    )
    cod_conaliteg = CharField(
        verbose_name=_("Codigo CONALITEG"),
        max_length=255,
    )
    language = models.CharField(
        verbose_name=_("Idioma"),
        choices=IDIOM_CHOICES,
        max_length=10,
        default=_("es"),
    )
    isbn = CharField(
        verbose_name=_("ISBN"),
        max_length=255,
        null=True,
        blank=True,
    )
    author = CharField(
        verbose_name=_("Autor"),
        max_length=255,
        null=True,
        blank=True,
    )
    editorial_team = CharField(
        verbose_name=_("Equipo Editorial"),
        max_length=255,
        null=True,
        blank=True,
    )
    first_edition = CharField(
        verbose_name=_("Primera Edición"),
        max_length=255,
        null=True,
        blank=True,
    )
    second_reprint = CharField(
        verbose_name=_("Segunda Reimpresión"),
        max_length=255,
        null=True,
        blank=True,
    )
    teacher_book = ForeignKey(
        get_document_model_string(),
        verbose_name=_("Libro del docente (Español)"),
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )
    teacher_book_english = ForeignKey(
        get_document_model_string(),
        verbose_name=_("Libro del docente (Inglés)"),
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )
    student_book = ForeignKey(
        "commons.ExternalRedirect",
        verbose_name=_("Libro del Estudiante"),
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )

    office_sep = ForeignKey(
        get_document_model_string(),
        verbose_name=_("Oficio SEP"),
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )
    video = URLField(
        verbose_name=_("Video"),
        null=True,
        blank=True,
    )
    teaching_dosage = ForeignKey(
        get_document_model_string(),
        verbose_name=_("Dosificación Docente"),
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )
    parent_programming = ForeignKey(
        get_document_model_string(),
        verbose_name=_("Programación para Padres"),
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )
    reader = ForeignKey(
        get_document_model_string(),
        verbose_name=_("Lector"),
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )
    audio = ForeignKey(
        get_document_model_string(),
        verbose_name=_("Audios"),
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )
    posters = ForeignKey(
        get_document_model_string(),
        verbose_name=_("Posters"),
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )
    title_description = CharField(
        verbose_name=_("Título de la descripción"),
        max_length=255,
        null=True,
        blank=True,
    )

    content_panels = (
        [BasePage.replace_content_field(CONTENT_FIELD)[0]]
        + [StreamFieldPanel("intro_detail_product")]
        + [BasePage.replace_content_field(CONTENT_FIELD)[-1]]
    )
    promote_panels = BasePage.promote_panels
    settings_panels = BasePage.settings_panels
    product_property = [
        MultiFieldPanel(
            [
                FieldPanel("title_description"),
                FieldPanel("short_description"),
                ImageOrSVGPanel("image"),
                SnippetChooserPanel("grade"),
                SnippetChooserPanel("subject"),
                SnippetChooserPanel("serie"),
                FieldPanel("campo_formacion"),
                FieldPanel("cod_conaliteg"),
                FieldPanel("language"),
                FieldPanel("isbn"),
                FieldPanel("author"),
                FieldPanel("editorial_team"),
                FieldPanel("first_edition"),
                FieldPanel("second_reprint"),
            ],
            heading=_("Detalles del Libro"),
        ),
        MultiFieldPanel(
            [
                DocumentChooserPanel("teacher_book"),
                DocumentChooserPanel("teacher_book_english"),
                DocumentChooserPanel("student_book"),
                DocumentChooserPanel("office_sep"),
                FieldPanel("video"),
                DocumentChooserPanel("teaching_dosage"),
                DocumentChooserPanel("parent_programming"),
                DocumentChooserPanel("reader"),
                DocumentChooserPanel("audio"),
                DocumentChooserPanel("posters"),
            ],
            heading=_("Materiales"),
        ),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading=_("Contenido")),
            ObjectList(promote_panels, heading=_("Promocionar")),
            ObjectList(settings_panels, heading=_("Propiedades"), classname="settings"),
            ObjectList(product_property, heading=_("Propiedad del producto")),
            ObjectList(
                [FieldPanel("thematic_content")], heading=_("Contenidos Tematicos")
            ),
        ]
    )

    subpage_types = []

    class Meta:
        verbose_name = _("Detalle de Producto")
        verbose_name_plural = _("Detalles de Productos")

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["related_pages"] = (
            DetailProductPage.objects.filter(subject=self.subject)
            .exclude(id=self.id)
            .live()
        )
        context["related_degrees"] = Degree.objects.exclude(name=self.grade)
        return context


class DetailArticlePage(BasePage):
    """Model for the detail article page."""

    CONTENT_FIELD = "_content_detail_article"

    _content_detail_article = StreamField(
        [], verbose_name=("Contenido"), null=True, blank=True
    )

    content_panels = BasePage.replace_content_field(CONTENT_FIELD)

    subpage_types = []

    class Meta:
        verbose_name = _("Detalle de artículo")
        verbose_name_plural = _("Detalles de artículos")


class ExternalRedirect(BasePage):
    """Define una página que redirecciona a una URL externa."""

    subpage_types = [
        "commons.ExternalRedirect",
    ]
    redirect_url = models.URLField()
    content_panels = Page.content_panels + [FieldPanel("redirect_url")]

    class Meta(Page.Meta):
        """Define properties for Page."""

        verbose_name = _("Redirección")
        verbose_name_plural = _("Redirecciones")

    def serve(self, request, *args, **kwargs):
        """Return a permanent redirect response."""
        return HttpResponsePermanentRedirect(self.redirect_url)
