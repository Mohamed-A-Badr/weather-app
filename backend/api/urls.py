from django.urls import path
from .views import weather_api_view

urlpatterns = [
    path('weather/', weather_api_view, name='weather'),
]