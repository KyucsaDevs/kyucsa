# your_app/signals.py
# from django.core.mail import send_mail
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags
# from django.utils import timezone
# from .models import Event
from django.db.models.signals import pre_save
#from django.core.mail import send_mail
from django.db import transaction
from .models import KyucsaIdCounter

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

# @receiver(post_save, sender=Event)
# def send_event_notification(sender, instance, created, **kwargs):
#     if created:  # Only send email on event creation, not updates
#         subject = 'New Event Notification'
#         context = {'event': instance, 'current_time': timezone.now()}
#         message = render_to_string('email/event_notification.txt', context)
#         plain_message = strip_tags(message)
#         from_email = 'your_email@example.com'  # Change this to your email
#         recipient_list = ['user1@example.com', 'user2@example.com']  # Add the actual recipients
#         send_mail(subject, plain_message, from_email, recipient_list, html_message=message)