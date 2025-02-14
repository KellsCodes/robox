from django.urls import path
from . import views

urlpatterns = [
    path("settings", views.UserSettingsView.as_view(),  name="app-settings")
]
