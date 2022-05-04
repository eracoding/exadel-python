from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Roles Table
class Roles(models.Model):
    COMPANY = 'COMPANY'
    USER = 'USER'
    Name = models.CharField(
        max_length=8,
        choices=[(COMPANY, 'Company'), (USER, 'Ordinary User')],
        default=USER,
    )

    def __unicode__(self):
        return self.Name

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'


# RequestStatus table
class RequestStatus(models.Model):
    PENDING = 'PENDING'
    CANCELED = 'CANCELED'
    COMPLETED = 'COMPLETED'
    Status = models.CharField(
        max_length=9,
        choices=[(PENDING, 'Pending'), (CANCELED, 'Canceled'), (COMPLETED, 'Completed')],
    )

    def __unicode__(self):
        return self.Status

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = 'RequestStatus'
        verbose_name_plural = 'RequestStatuses'


# User table
class User(models.Model):
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    role = models.OneToOneField(Roles, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'%s, %s, %s, %s' % (self.fullname, self.phone, self.email, self.role)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


# Service table
class Service(models.Model):
    Name = models.CharField(max_length=255)
    Cost = models.DecimalField(max_length=6, decimal_places=2)
    company_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'%s, %s' % (self.Name, self.Cost)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


# Request table
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


# Review table
class Review(models.Model):
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    request_id = models.ForeignKey(Request, unique=True, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, unique=True, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'%s, %s, %s' % (self.rating, self.feedback, self.created_at)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
