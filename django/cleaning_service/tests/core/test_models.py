import json
import pytest

from core.models import User


pytestmark = pytest.mark.django_db


class TestUserEndpoints:

    endpoint = '/api/user/'

    def test_list(self, api_client, uubb):
        client = api_client()
        uubb(3)
        url = self.endpoint
        response = client.get(url)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3

    def test_create(self, api_client, uubb):
        client = api_client()
        t = uubb(1)[0]
        valid_data_dict = {
            'password': t.password,
            'role': t.role.name,
            'fullname': t.fullname,
            'email': t.email,
            'phone': t.phone
        }

        url = f'{self.endpoint}create/'

        response = client.post(
            url,
            valid_data_dict,
            format='json'
        )

        assert response.status_code == 201
        assert json.loads(response.content) == valid_data_dict
        assert User.objects.last().link

    def test_retrieve(self, api_client, fub):
        t = fub()
        t = User.objects.last()
        expected_json = t.__dict__
        expected_json['role'] = t.role.name

        expected_json.pop('_state')
        expected_json.pop('user_id')
        url = f'{self.endpoint}{t.id}/'

        response = api_client().get(url)

        assert response.status_code == 200 or response.status_code == 301
        assert json.loads(response.content) == expected_json

    def test_delete(self, api_client, uubb):
        user = uubb(1)[0]
        url = f'{self.endpoint}{user.id}/delete/'

        response = api_client().delete(
            url
        )

        assert response.status_code == 204 or response.status_code == 301
