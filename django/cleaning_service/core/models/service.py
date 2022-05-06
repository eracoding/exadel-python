from django.db import models
from .user import User


class Service(models.Model):
    name = models.CharField(max_length=255, null=False)
    cost = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    company_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __unicode__(self):
        return u'%s, %s' % (self.name, self.cost)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'