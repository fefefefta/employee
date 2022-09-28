from rest_framework import parsers, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from .models import Profile
from .serializers import UserAvatarSerializer, ProfileSerializer


class UserAvatar(ModelViewSet):
    """Создание и обновление аватара профиля"""

    parser_classes = [parsers.MultiPartParser]
    serializer_class = UserAvatarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.filter(id=self.request.user.id)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)
        return obj


class ProfileViewSet(ModelViewSet):
    """CRUD профиля"""
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(id=self.request.user.id)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)
        return obj
