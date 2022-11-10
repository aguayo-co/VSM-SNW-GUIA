from django.forms import (
    CharField,
    ChoiceField,
    Form,
    ModelChoiceField,
    ModelMultipleChoiceField,
)
from django.utils.translation import gettext_lazy as _

from commons.models import CatalogPage, Degree, Serie, Subject
from commons.templatetags.catalog_tags import get_catalog_page


class CatalogFilterForm(Form):
    grade = ModelMultipleChoiceField(Degree.objects, label=_("Grados"), required=False)
    subject = ModelMultipleChoiceField(
        Subject.objects, label=_("Materias"), required=False
    )
    serie = ModelMultipleChoiceField(Serie.objects, label=_("Series"), required=False)


class SearchForm(Form):
    query = CharField(min_length=3)
    type = ChoiceField(
        choices=(
            ("", "Todo el sitio web"),
            ("catalog", CatalogPage.objects.live().first().title),
        )
    )
