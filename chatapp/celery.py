# celery.py

import os
from celery import Celery
from datetime import timedelta 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatapp.settings')

app = Celery('chatapp')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# celery -A chatapp worker --loglevel=info
# celery -A chatapp beat --loglevel=info
# above line are required to start celery