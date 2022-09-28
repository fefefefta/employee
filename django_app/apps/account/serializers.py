from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile


class UserAvatarSerializer(serializers.ModelSerializer):
    """Аватар профиля"""
    avatar = serializers.ImageField()

    class Meta:
        model = Profile
        fields = [
            "id",
            "avatar"
        ]


class UserSerializer(serializers.ModelSerializer):
    """Стандартная пользовательская модель"""

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name"
        ]


class ProfileSerializer(serializers.ModelSerializer):
    """Профиль"""
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "birthday",
            "bio",
            "phone",
            "departament",
        ]
