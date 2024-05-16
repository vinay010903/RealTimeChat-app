# tasks.py
from celery import shared_task
from .models import Room, Message

@shared_task
def delete_excess_messages():
    for room in Room.objects.all():
        messages = Message.objects.filter(room=room).order_by('id')
        if messages.count() > 10:
            excess_messages = messages[:-10]
            excess_messages.delete()