from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Trade
from .trade_serializer import TradeSerializer
# Create your views here.


class TradeViewSet(ModelViewSet):
    """List, create, update, delete trade journals"""
    permission_classes = [IsAuthenticated]
    serializer_class = TradeSerializer

    def get_queryset(self):
        """filter trades to show only authenticated users trades"""
        return Trade.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Ensure the logged-in user is the owner of the trade"""
        serializer.save(user=self.request.user)
