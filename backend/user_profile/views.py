from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .profile_serializer import ProfileSerializer
from .models import UserProfileModel
# Create your views here.


class UserProfileView(APIView):
    """Create, Update, get user profile"""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """Create profile"""
        data = request.data.copy()
        data["user"] = request.user.id
        serializer = ProfileSerializer(data=data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user)
            return Response({"message": "Profile saved", "data": serializer.data})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        """Update user profile"""
        profile = get_object_or_404(
            UserProfileModel, user=request.user)
        serializer = ProfileSerializer(
            profile, data=request.data, partial=True)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"code": 1, "data": serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """Fetch user profile"""
        try:
            profile = get_object_or_404(
                UserProfileModel, user=request.user)
            serializer = ProfileSerializer(profile)
            return Response({"code": 1, "data": serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
