from rest_framework import serializers
from .models import UserAppSettings


class SettingsSerializer(serializers.ModelSerializer):
    """Settings serializer"""
    class Meta:
        model = UserAppSettings
        fields = ["id", "news_update", "economic_data", "trade_outcome"]
