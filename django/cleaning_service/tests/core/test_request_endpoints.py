import json
import pytest
from model_bakery import baker
from core.models import RequestModel, RequestStatus

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

        response = api_client().post('/api/request', payload)

        request_from_db = RequestModel.objects.all().first()

        assert response.status_code == 201 or response.status_code == 301
        assert payload["address"] == request_from_db.address

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
        auth_client.put(f'/api/request/{request.id}', payload2)

        request_from_db = RequestModel.objects.all().first()

        assert request_from_db.address == payload['address']

