from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    name_school = CharField(
        verbose_name=_("Nombre de la escuela"),
        max_length=255,
        null=True,
        blank=True
    )
    work_center_key = CharField(
        verbose_name=_("Clave del Centro de Trabajo"),
        max_length=255,
        null=True,
        blank=True
    )
    grade_attends = CharField(
        verbose_name=_("Grado que atiende"),
        max_length=255,
        null=True,
        blank=True
    )
    federal_entity = CharField(
        verbose_name=_("Entidad Federativa"),
        max_length=255,
        null=True,
        blank=True
    )
    phone = CharField(
        verbose_name=_("Teléfono"),
        max_length=255,
        null=True,
        blank=True
    )


