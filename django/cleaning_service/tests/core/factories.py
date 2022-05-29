import pytest
from model_bakery import baker


def uubb():
    def unfilled_user_bakery_batch(n):
        uubb = baker.make(
            'core.User',
            _quantity=n
        )
        return uubb

    return unfilled_user_bakery_batch


@pytest.fixture
def fubb():
    def filled_user_bakery_batch(n):
        uubb = baker.make(
            'core.User',
            _quantity=n
        )
        return uubb

    return filled_user_bakery_batch


@pytest.fixture
def fub():
    def filled_user_bakery():
        uubb = baker.make(
            'core.User',
            role=baker.make('core.Roles')
        )
        return uubb

    return filled_user_bakery
