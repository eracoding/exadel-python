import json
import pytest
from model_bakery import baker
from core.models import User, Roles

pytestmark = pytest.mark.django_db


class TestUserEndpoints:

    endpoint = '/api/user/'

    def test_list(self, api_client):
        baker.make(User, _quantity=3)
        response = api_client().get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3

    def test_create(self, api_client):
        user = baker.make(User)
        user.role = Roles.objects.get(name=1)
        payload = dict(
            fullname=user.fullname,
            email=user.email,
            password=user.password,
            phone=user.phone,
            role=user.role
        )

        response = api_client().post('/auth/users', payload)
        user_from_db = User.objects.all().first()

        assert response.status_code == 201 or response.status_code == 301
        assert payload["fullname"] == user_from_db.fullname

    def test_retrieve(self, api_client):
        user = baker.make(User)
        user.role = Roles.objects.get(name=1)
        payload = dict(
            fullname=user.fullname,
            email=user.email,
            password=user.password,
            phone=user.phone,
            role=user.role
        )
        api_client().post('/api/user/create', payload)

        response = api_client().get(f'/api/user/{user.id}')

        assert response.data["email"] == payload["email"]
        assert response.status_code == 200

    def test_not_found(self, api_client):
        user = baker.make(User)
        user.role = Roles.objects.get(name=1)
        payload = dict(
            fullname=user.fullname,
            email=user.email,
            password=user.password,
            phone=user.phone,
            role=user.role
        )
        api_client().post('/api/user/create', payload)

        response = api_client().get(f'/api/user/{user.id+1}')

        assert response.status_code == 404

    def test_update(self, api_client):
        user = baker.make(User)
        user.role = Roles.objects.get(name=1)
        payload = dict(
            fullname=user.fullname,
            email=user.email,
            password=user.password,
            phone=user.phone,
            role=user.role
        )
        api_client().post('/api/user/create', payload)

        payload2 = dict(
            phone='1234'
        )
        api_client().put(f'/api/user/{user.id}/update/', payload2)
        user_from_db = User.objects.all().first()

        assert user_from_db.phone == payload['phone']

    def test_delete(self, auth_client):
        user = User.objects.create(fullname='Kate Jorney', email='kate@mail.com', password='kate', phone='12345',
                                   role=Roles.objects.get(name=1))
        response = auth_client.delete(f'{self.endpoint}{user.id}/delete')

        assert response.status_code == 204

        with pytest.raises(User.DoesNotExist):
            user.refresh_from_db()

    def test_missing_value(self, auth_client):
        user = baker.make(User)
        payload = dict(
            email=user.email,
            password=user.password,
            phone=user.phone,
            role=user.role
        )

        response = auth_client.post('/api/user/create', payload)

        assert response.status_code == 400
