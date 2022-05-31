import json
import pytest
from model_bakery import baker
from core.models import RequestModel

pytestmark = pytest.mark.django_db


class TestRequestEndpoint:

    endpoint = '/api/request/'

    def test_list(self, auth_client):
        baker.make(RequestModel, _quantity=3)
        response = auth_client.get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3

    def test_create_auth(self, api_client, auth_client):
        client = auth_client

        request = baker.make(RequestModel)
        payload = dict(
            area_total=request.area_total,
            cost_total=request.cost_total,
            address=request.address
        )

        response = client.post('/api/request', payload)

        request_from_db = RequestModel.objects.all().first()

        assert response.status_code == 201 or response.status_code == 301
        assert payload["address"] == request_from_db.address

    def test_create_unauth(self, api_client):
        request = baker.make(RequestModel)
        payload = dict(
            area_total=request.area_total,
            cost_total=request.cost_total,
            address=request.address
        )

        response = api_client().post(self.endpoint, payload)

        request_from_db = RequestModel.objects.all().first()

        assert response.status_code == 401 or response.status_code == 403

    def test_retrieve(self, auth_client, api_client):
        request = baker.make(RequestModel)
        payload = dict(
            area_total=request.area_total,
            cost_total=request.cost_total,
            address=request.address
        )
        auth_client.post('/api/request', payload)

        response = api_client().get(f'/api/request/{request.id}')

        request_from_db = RequestModel.objects.all().first()

        assert request_from_db.address == payload["address"]
        assert response.status_code == 200

    def test_update(self, api_client, auth_client):
        client = auth_client
        request = baker.make(RequestModel)
        payload = dict(
            area_total=request.area_total,
            cost_total=request.cost_total,
            address=request.address
        )

        api_client().post('/api/request/create', payload)

        payload2 = dict(
            address='abcd'
        )
        auth_client.put(f'/api/request/{request.id}/update', payload2)

        request_from_db = RequestModel.objects.all().first()

        assert request_from_db.address == payload['address']

    def test_delete(self, auth_client):
        request = baker.make(RequestModel)
        response = auth_client.delete(f'{self.endpoint}{request.id}/delete')

        assert response.status_code == 204

    def test_not_found(self, api_client, auth_client):
        request = baker.make(RequestModel)
        payload = dict(
            area_total=request.area_total,
            cost_total=request.cost_total,
            address=request.address
        )
        auth_client.post('/api/request', payload)

        response = api_client().get(f'/api/request/{request.id+1}')

        assert response.status_code == 404

    def test_missing_value(self, auth_client):
        request = baker.make(RequestModel)
        payload = dict(
            area_total=request.area_total,
            cost_total=request.cost_total   # address is missing
        )
        response = auth_client.post('/api/request/create', payload)

        assert response.status_code == 400

