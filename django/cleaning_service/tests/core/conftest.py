import pytest
from rest_framework.test import APIClient
from django.conf import settings


def pytest_configure():
    settings.configure(DATABASES=...)


@pytest.fixture
def api_client():
    return APIClient
