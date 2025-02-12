from rest_framework import serializers
from .models import UserProfileModel


class ProfileSerializer(serializers.ModelSerializer):
    """Update or get profile serializer"""
    profile_img = serializers.ImageField(required=False)

    class Meta:
        model = UserProfileModel
        fields = "__all__"
        read_only_fields = ['user']
