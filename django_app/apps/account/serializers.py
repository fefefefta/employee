from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile, Achievement


class UserSerializer(serializers.ModelSerializer):
    """Стандартная пользовательская модель"""

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name"
        ]


class AchievementSerializer(serializers.ModelSerializer):
    """Достижения"""

    class Meta:
        model = Achievement
        fields = [
            "id",
            "icon",
            "name",
            "description"
        ]


class ProfileSerializer(serializers.ModelSerializer):
    """Профиль"""
    user = UserSerializer()
    position = serializers.CharField()
    achievements = AchievementSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "avatar",
            "birthday",
            "bio",
            "phone",
            "position",
            "departament",
            "achievements",
        ]
