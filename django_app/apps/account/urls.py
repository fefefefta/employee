from rest_framework import routers
from django.urls import path, include

from .views import ProfileViewSet

router = routers.SimpleRouter()
router.register(r'user', ProfileViewSet, basename="profile")

urlpatterns = [
    path('', include(router.urls)),
]
