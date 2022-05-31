from django.db import models
from .requestStatus import RequestStatus
from .user import User


class RequestModel(models.Model):
    area_total = models.IntegerField(null=False)
    cost_total = models.DecimalField(max_digits=8, decimal_places=2 ,null=False)
    address = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    requestStatus_id = models.OneToOneField(RequestStatus, on_delete=models.CASCADE, null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
    company_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='company_id')

    def __unicode__(self):
        return u'%s, %s, %s, %s' % (self.user_id, self.address, self.area_total, self.cost_total)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = 'Request Model'
        verbose_name_plural = 'Request Models'
