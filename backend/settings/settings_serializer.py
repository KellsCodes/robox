from rest_framework import serializers
from .models import UserAppSettings


class SettingsSerializer(serializers.ModelSerializer):
    """Settings serializer"""
    class Meta:
        model = UserAppSettings
        fields = ["id", "new_updates", "economic_data", "trade_outcome"]

    def validate(self, data):
        """Custom validation for boolean fields"""
        for field, value in data.items():
            if value not in [True, False, 1, 0]:
                raise serializers.ValidationError(
                    {field: f"{field} must be either true or false."})
        return data
