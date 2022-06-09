from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .request import RequestModel
from .service import Service
from .user import User


class Review(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=False, default=0)
    feedback = models.TextField(null=False, default='No Feedback')
    created_at = models.DateTimeField(auto_now_add=True)
    request_id = models.OneToOneField(RequestModel, on_delete=models.CASCADE, null=False)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE, null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __unicode__(self):
        return u'%s, %s, %s' % (self.rating, self.feedback, self.created_at)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
