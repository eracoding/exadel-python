from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from request import Request
from service import Service
from user import User


class Review(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    request_id = models.ForeignKey(Request, unique=True, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'%s, %s, %s' % (self.rating, self.feedback, self.created_at)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
