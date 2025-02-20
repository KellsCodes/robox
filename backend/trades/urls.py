from django.urls import path
from .views import TradeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("journals", TradeViewSet, basename="journal")

urlpatterns = router.urls
