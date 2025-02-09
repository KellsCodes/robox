from django.db import models
from django.contrib.auth.models import AbstractUser
from .custom_user_manager import CustomUserManager

# Create your models here.


class UserAccount(AbstractUser):
    """Create user class"""
    email = models.EmailField(
        max_length=255, unique=True, verbose_name='Email Address')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
