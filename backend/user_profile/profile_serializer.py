from rest_framework import serializers
from .models import UserProfileModel


class ProfileSerializer(serializers.ModelSerializer):
    """Update or get profile serializer"""
    profile_img = serializers.ImageField(required=False)
    email = serializers.EmailField(source="user.email", read_only=True)
    user_id = serializers.CharField(source="user.id", read_only=True)

    class Meta:
        model = UserProfileModel
        fields = ["id", "first_name", "last_name", "display_name", "profile_img",
                  "country", "state", "city", "address", "email", "user_id"]
