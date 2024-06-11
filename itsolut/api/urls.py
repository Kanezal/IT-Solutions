from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import AdvertisementViewAPI

urlpatterns = [
    path('advertisement/', AdvertisementViewAPI.as_view(), name='advertisement'),
]
