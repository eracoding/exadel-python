from django.db import models
from django.utils.translation import gettext_lazy as _


class Roles(models.Model):

    class RolesEnum(models.IntegerChoices):
        USER = 1, _("Ordinary User")
        COMPANY = 2, _("Company")

    name = models.IntegerField(
        choices=RolesEnum.choices,
        default=RolesEnum.USER,
    )

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'
