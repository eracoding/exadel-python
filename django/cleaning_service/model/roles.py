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

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'