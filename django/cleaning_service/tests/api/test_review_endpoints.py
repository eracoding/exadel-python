import json
import pytest
from model_bakery import baker
from core.models import Review

pytestmark = pytest.mark.django_db


class TestReviewsEndpoint:

    endpoint = '/api/review/'

    def test_list(self, api_client):
        baker.make(Review, _quantity=3)
        response = api_client().get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3

    def test_create_auth(self, api_client, auth_client):
        client = auth_client

        review = baker.make(Review)
        payload = dict(
            rating=review.rating,
            feedback=review.feedback
        )

        response = client.post('/api/review', payload)

        review_from_db = Review.objects.all().first()

        assert response.status_code == 201 or response.status_code == 301
        assert payload["feedback"] == review_from_db.feedback

    def test_create_unauth(self, api_client):
        review = baker.make(Review)
        payload = dict(
            rating=review.rating,
            feedback=review.feedback
        )

        response = api_client().post(self.endpoint, payload)

        review_from_db = Review.objects.all().first()

        assert response.status_code == 403 or response.status_code == 401

    def test_retrieve(self, api_client, auth_client):
        review = baker.make(Review)
        payload = dict(
            rating=review.rating,
            feedback=review.feedback
        )

        auth_client.post('/api/review/create', payload)

        response = api_client().get(f'/api/review/{review.id}')

        service_from_db = Review.objects.all().first()

        assert service_from_db.id == review.id
        assert response.status_code == 200

    def test_update(self, auth_client):
        client = auth_client
        review = baker.make(Review)
        payload = dict(
            rating=review.rating,
            feedback=review.feedback
        )

        auth_client.post('/api/review/create', payload)

        payload2 = dict(
            feedback='abcd'
        )
        auth_client.put(f'/api/review/{review.id}/update/', payload2)

        service_from_db = Review.objects.all().first()

        assert service_from_db.feedback == payload['feedback']

    def test_delete(self, auth_client):
        review = baker.make(Review)
        response = auth_client.delete(f'{self.endpoint}{review.id}/delete')

        assert response.status_code == 204

    def test_not_found(self, api_client, auth_client):
        review = baker.make(Review)
        payload = dict(
            rating=review.rating,
            feedback=review.feedback
        )
        auth_client.post('/api/review', payload)

        response = api_client().get(f'/api/review/{review.id+1}')

        assert response.status_code == 404

    def test_missing_value(self, auth_client):
        review = baker.make(Review)
        payload = dict(
            rating=review.rating
        )
        response = auth_client.post('/api/review/create', payload)

        assert response.status_code == 400
