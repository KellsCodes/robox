from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import UserAppSettings
from .settings_serializer import SettingsSerializer

# Create your views here.


class UserSettingsView(APIView):
    """settings class"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            settings = get_object_or_404(UserAppSettings, user=request.user)
            serializer = SettingsSerializer(settings)
            return Response({"code": 1, "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e), "code": 3}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            settings = get_object_or_404(UserAppSettings, user=request.user)
            serializer = SettingsSerializer(
                settings, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"code": 1, "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e), "code": 3}, status=status.HTTP_400_BAD_REQUEST)
