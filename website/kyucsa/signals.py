# your_app/signals.py
import uuid
import datetime
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.db import transaction
from .models import StudentRegistration, KyucsaIdCounter

def generateKyucsaId():
    with transaction.atomic():
        counter, created = KyucsaIdCounter.objects.select_for_update().get_or_create()
        counter.last_used_id += 1
        counter.save()
        return f'{counter.last_used_id:06}'

def sendKyucsaIdEmail(email, kyucsaId):
    return False
    # send_mail(
    #     'Your Kyucsa ID',
    #     f'Your Kyucsa ID is: {kyucsaId}',
    #     'from@example.com',
    #     [email],
    #     fail_silently=False,
    # )
