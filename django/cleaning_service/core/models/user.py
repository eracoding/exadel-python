from django.db import models
from .roles import Roles


class User(models.Model):
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE, null=False)

    def __unicode__(self):
        return u'%s, %s, %s, %s' % (self.fullname, self.phone, self.email, self.role)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
