import pytest
from core.models import User, Service, RequestModel, Roles, RequestStatus, Review
from faker import Faker

fake = Faker()


@pytest.mark.django_db
def test_user(user_factory):
    user = user_factory.build()
    role = Roles.objects.get(name=1)
    user.role = role
    user.save()
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_service(service_factory, user_factory):
    service = service_factory.build()
    service.company_id = user_factory.create()
    service.save()
    assert Service.objects.count() == 1


@pytest.mark.django_db
def test_request(request_factory, user_factory, service_factory):
    req = request_factory.build()
    req.user_id = user_factory.create()
    company = user_factory.build()
    company.email = fake.email()

    service = service_factory.build()
    service.company_id = company

    req.service_id = service
    req.requestStatus_id = RequestStatus.objects.get(status=1)

    company.save()
    service.save()
    req.save()
    assert RequestModel.objects.count() == 1


@pytest.mark.django_db
def test_review(review_factory, service_factory, user_factory, request_factory):
    user = user_factory.build()
    role = Roles.objects.get(name=1)
    user.role = role
    user.email = fake.email()

    company = user_factory.build()
    company.role = role
    company.email = fake.email()

    service = service_factory.build()
    service.company_id = company

    req = request_factory.build()
    req.user_id = user
    req.service_id = service
    req.requestStatus_id = RequestStatus.objects.get(status=1)

    review = review_factory.build()
    review.user_id = user
    review.request_id = req
    review.service_id = service

    user.save()
    company.save()
    service.save()
    req.save()
    review.save()
    assert Review.objects.count() == 1
