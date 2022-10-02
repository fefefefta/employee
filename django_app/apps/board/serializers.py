from django.contrib.auth.models import User
from rest_framework import serializers

from . import models
from apps.account.models import Profile


class UserSerializer(serializers.ModelSerializer):
    """Стандартная пользовательская модель"""

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name"
        ]
        ref_name = 'board_user'


class ProfileSerializer(serializers.ModelSerializer):
    """Профиль"""
    user = UserSerializer()
    position = serializers.CharField()

    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "avatar",
            "position",
        ]
        ref_name = 'board_profile'


class DepartamentSerializer(serializers.ModelSerializer):
    """Отдел"""

    class Meta:
        model = models.Departament
        fields = [
            "id",
            "name"
        ]


class PaymentSerializer(serializers.ModelSerializer):
    """Оплата"""

    class Meta:
        model = models.Payment
        fields = [
            "id",
            "user",
            "idea"
        ]


class LocationSerializer(serializers.ModelSerializer):
    """Адрес"""

    class Meta:
        model = models.Location
        fields = [
            "city",
            "street",
            "house"
        ]


class ImageSerializer(serializers.ModelSerializer):
    """Изображение"""

    class Meta:
        model = models.Image
        fields = [
            "id",
            "image"
        ]


class FileSerializer(serializers.ModelSerializer):
    """Файл"""

    class Meta:
        model = models.File
        fields = [
            "id",
            "file"
        ]


class EventListSerializer(serializers.ModelSerializer):
    """Список событий"""

    class Meta:
        model = models.Event
        fields = [
            "id",
            "name",
            "start",
            "end",
            "description"
        ]


class EventDetailSerializer(serializers.ModelSerializer):
    """Событие"""
    payment = PaymentSerializer()
    location = LocationSerializer()
    image = ImageSerializer()

    class Meta:
        model = models.Event
        fields = [
            "id",
            "name",
            "start",
            "end",
            "description",
            "location",
            "payment",
            "image",
        ]


class CategorySerializer(serializers.ModelSerializer):
    """Категория"""

    class Meta:
        model = models.Idea
        fields = [
            "id",
            "name"
        ]


class IdeaListSerializer(serializers.ModelSerializer):
    """Список идей"""
    profile = serializers.SerializerMethodField()
    file = FileSerializer(many=True, read_only=True)
    category = CategorySerializer()

    class Meta:
        model = models.Idea
        fields = [
            "id",
            'profile',
            "category",
            "name",
            "created",
            "description",
            "likes",
            "user_likes",
            "status",
            "file",
        ]

    def get_profile(self, obj):
        profile = Profile.objects.get(user_id=obj.id)
        serializer = ProfileSerializer(profile)
        return serializer.data
