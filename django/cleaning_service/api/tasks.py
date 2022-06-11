from celery.utils.log import get_task_logger
from core.models import User
from model_bakery import baker
from final_project.celery import app
from core.utility import Util

logger = get_task_logger(__name__)


@app.task(name='create_users')
def create_users(n):
    users = baker.make(User, _quantity=n)
    return n


@app.task(name='send_email_task')
def send_email_task(data):
    logger.info("Sending activation email")
    return Util.send_email(data)
