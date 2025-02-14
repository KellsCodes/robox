from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .profile_serializer import ProfileSerializer
# Create your views here.


class UserProfileView(APIView):
    """Create, Update, get user profile"""
    print("hello")
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
