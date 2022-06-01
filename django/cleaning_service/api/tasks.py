from core.models import User
from model_bakery import baker
from celery import shared_task


@shared_task
def create_users(n):
    baker.make(User, _quantity=n)
    return f'{n} random users created with success!'
