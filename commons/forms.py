from django.forms import Form, ModelChoiceField, ModelMultipleChoiceField

from django.utils.translation import gettext_lazy as _
from commons.models import Degree, Subject, Serie


class CatalogFilterForm(Form):
    grade = ModelMultipleChoiceField(Degree.objects, label=_("Grados"), required=False)
    subject = ModelMultipleChoiceField(Subject.objects, label=_("Materias"), required=False)
    serie = ModelMultipleChoiceField(Serie.objects, label=_("Series"), required=False)
