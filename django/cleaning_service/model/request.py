from django.db import models
from requestStatus import RequestStatus
from user import User


class Request(models.Model):
    area_total = models.IntegerField()
    cost_total = models.DecimalField(max_length=8, decimal_places=2)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    requestStatus_id = models.OneToOneField(RequestStatus, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    company_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'%s, %s, %s' % (self.address, self.area_total, self.cost_total)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'
