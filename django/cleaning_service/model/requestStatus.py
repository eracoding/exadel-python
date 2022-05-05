from django.db import models
from django.utils.translation import gettext_lazy as _


class RequestStatus(models.Model):

    class RequestStatusEnum(models.IntegerChoices):
        PENDING = 1, _('PENDING')
        CANCELED = 2, _('CANCELED')
        COMPLETED = 3, _('COMPLETED')

    status = models.IntegerField(
        choices=RequestStatusEnum.choices,
    )

    def __unicode__(self):
        return self.status

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = 'Request Status'
        verbose_name_plural = 'Request Statuses'

