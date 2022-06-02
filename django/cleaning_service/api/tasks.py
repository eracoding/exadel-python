from core.models import User
from model_bakery import baker
from final_project.celery import app


@app.task(name='create_users')
def create_users(n):
    users = baker.make(User, _quantity=n)
    return n
