import factory

from core.models import User, Review, RequestModel, Service
from faker import Faker

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    fullname = fake.name()
    email = fake.email()
    password = fake.password()
    phone = fake.phone_number()


class RequestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RequestModel

    area_total = fake.ean(length=8)
    cost_total = '14.5'


class ServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Service

    name = fake.pystr()
    cost = 10.0


class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Review

    rating = 5
    feedback = fake.paragraph()
