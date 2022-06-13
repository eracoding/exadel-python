from django.db import models
from .requestStatus import RequestStatus
from .user import User
from .service import Service


class RequestModel(models.Model):
    area_total = models.IntegerField(null=False)
    cost_total = models.IntegerField(null=False)
    address = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    requestStatus_id = models.ForeignKey(RequestStatus, on_delete=models.CASCADE, null=False, default=1)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE, null=False, related_name='service_id')

    def __unicode__(self):
        return u'Request: %s, %s, %s, %s' % (self.user_id, self.address, self.area_total, self.cost_total)

    def __str__(self):
        return self.__unicode__()

    def save(self, *args, **kwargs):
        self.cost_total = self.area_total * self.service_id.cost
        super(RequestModel, self).save()

    class Meta:
        verbose_name = 'Request Model'
        verbose_name_plural = 'Request Models'
