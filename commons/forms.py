from django.forms import Form, ModelChoiceField

from django.utils.translation import gettext_lazy as _
from commons.models import Degree, Subject, Serie


class CatalogFilterForm(Form):
    grade = ModelChoiceField(Degree.objects, label=_("Grados"), required=False)
    subject = ModelChoiceField(Subject.objects, label=_("Materias"), required=False)
    serie = ModelChoiceField(Serie.objects, label=_("Series"), required=False)
