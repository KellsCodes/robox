from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """Create and save a user with the email and password"""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The email field is required.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_super_user(self, email, password=None, **extra_fields):
        """Create and save SuperUser with email and password"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_super_user(email, password, **extra_fields)
