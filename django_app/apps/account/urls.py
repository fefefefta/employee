from rest_framework import routers
from django.urls import path, include

from .views import UserAvatar, ProfileViewSet

router = routers.SimpleRouter()
router.register(r'user', ProfileViewSet, basename="profile")

urlpatterns = [
    path('avatar/', UserAvatar.as_view({'put': 'update', 'post': 'create'})),
    path('', include(router.urls)),
]
