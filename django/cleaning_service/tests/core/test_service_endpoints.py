import json
import pytest
from model_bakery import baker
from core.models import Service

pytestmark = pytest.mark.django_db


class TestServicesEndpoint:

    endpoint = '/api/service/'

    def test_list(self, api_client):
        baker.make(Service, _quantity=3)
        response = api_client().get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3

    def test_create_auth(self, api_client, auth_client):
        client = auth_client

        service = baker.make(Service)
        payload = dict(
            name=service.name,
            cost=service.cost
        )

        response = client.post('/api/service', payload)

        service_from_db = Service.objects.all().first()

        assert response.status_code == 201 or response.status_code == 301
        assert payload["name"] == service_from_db.name

    def test_create_unauth(self, api_client):
        service = baker.make(Service)
        payload = dict(
            name=service.name,
            cost=service.cost
        )

        response = api_client().post(self.endpoint, payload)

        service_from_db = Service.objects.all().first()

        assert response.status_code == 401 or response.status_code == 403

    def test_retrieve(self, api_client):
        service = baker.make(Service)
        payload = dict(
            name=service.name,
            cost=service.cost
        )

        api_client().post(f'{self.endpoint}create', payload)

        response = api_client().get(f'{self.endpoint}{service.id}')

        service_from_db = Service.objects.all().first()

        assert service_from_db.id == service.id
        assert response.status_code == 200

    def test_update(self, api_client, auth_client):
        client = auth_client
        service = baker.make(Service)

        payload = dict(
            name=service.name,
            cost=service.cost
        )

        api_client().post(f'{self.endpoint}create', payload)

        payload2 = dict(
            name='abcd'
        )
        auth_client.put(f'{self.endpoint}{service.id}/update', payload2)

        service_from_db = Service.objects.all().first()

        assert service_from_db.name == payload['name']

    def test_delete(self, auth_client):
        service = baker.make(Service)
        response = auth_client.delete(f'{self.endpoint}{service.id}/delete')

        assert response.status_code == 204

    def test_not_found(self, api_client, auth_client):
        service = baker.make(Service)
        payload = dict(
            name=service.name,
            cost=service.cost
        )
        auth_client.post('/api/service', payload)

        response = api_client().get(f'/api/service/{service.id+1}')

        assert response.status_code == 404

    def test_missing_value(self, auth_client):
        service = baker.make(Service)
        payload = dict(
            cost=service.cost
        )

        response = auth_client.post('/api/service/create', payload)

        assert response.status_code == 400


