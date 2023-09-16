# your_app/signals.py
import uuid
import datetime
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Student

@receiver(pre_save, sender=Student)
def generate_registration_id(sender, instance, *args, **kwargs):
    if not instance.registration_id:
        current_year = datetime.datetime.now().year
        generated_numbers = uuid.uuid4().int & (1 << 31) - 1  # Generate random numbers
        instance.registration_id = f'CS{current_year}{generated_numbers:06}'
