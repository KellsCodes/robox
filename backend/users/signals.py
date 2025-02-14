# users/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from settings.models import UserAppSettings
from .models import UserAccount


@receiver(post_save, sender=UserAccount)
def create_user_settings(sender, instance, created, **kwargs):
    if created:
        UserAppSettings.objects.create(user=instance)
