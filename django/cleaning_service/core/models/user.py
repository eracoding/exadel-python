from django.db import models
from .roles import Roles
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, role, fullname, phone, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            role=role,
            fullname=fullname,
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, role, fullname, phone, password):

        if password is None:
            raise TypeError('Superusers must have a password.')
        roles = Roles.objects.get(name=role)
        user = self.create_user(
            email=self.normalize_email(email),
            role=roles,
            fullname=fullname,
            phone=phone,
            password=password)
        user.is_admin = True
        user.save()

        return user


class User(AbstractBaseUser):
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=255, unique=True)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE, null=False, default=1)
    password = models.CharField(max_length=255)
    username = None
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role', 'phone', 'fullname']

    def __unicode__(self):
        return u'%s, %s, %s' % (self.fullname, self.phone, self.email)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = 'User'
        db_table = 'User'
        verbose_name_plural = 'Users'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
