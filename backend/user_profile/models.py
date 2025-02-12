from django.db import models
from users.models import UserAccount

# Create your models here.


class UserProfileModel(models.Model):
    """Define profile model"""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user = models.OneToOneField(
        UserAccount, on_delete=models.CASCADE, related_name="profile")
    display_name = models.CharField(max_length=150)
    profile_img = models.ImageField(
        upload_to="profile_images/", max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
