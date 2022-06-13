import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_project.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
app = Celery('cleaning_service', broker='amqp://guest:guest@localhost:5672//', backend='amqp://',)
# app = Celery('cleaning_service', broker='amqp://user:password@rabbitmq3:5672//', backend='amqp://',)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
