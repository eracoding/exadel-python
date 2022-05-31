from pytest_factoryboy import register
from tests.core.factories import UserFactory, ReviewFactory, RequestFactory, ServiceFactory
from rest_framework.test import APIClient
from core.models import User, Roles
from model_bakery import baker
import pytest


register(UserFactory)
register(ReviewFactory)
register(RequestFactory)
register(ServiceFactory)


@pytest.fixture
def api_client():
    return APIClient


@pytest.fixture()
def auth_client():
    user = baker.make(User)
    client = APIClient()
    client.force_authenticate(user)
    return client
