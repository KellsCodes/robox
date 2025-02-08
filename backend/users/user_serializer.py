from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
User = get_user_model()


class UserSerializer(UserCreateSerializer):
    """Create user account serializer"""
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'created_at']
