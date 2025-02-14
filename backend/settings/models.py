from django.db import models
from users.models import UserAccount

# Create your models here.


class UserAppSettings(models.Model):
    """app preference settings"""
    news_update = models.BooleanField(default=True)
    economic_data = models.BooleanField(default=True)
    trade_outcome = models.BooleanField(default=True)
    user = models.OneToOneField(
        UserAccount, on_delete=models.CASCADE, related_name="settings")

    def __str__(self):
        return f"Settings for {self.user.email}"
