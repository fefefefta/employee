from rest_framework import serializers
from django.contrib.auth.models import User

from . import models
from apps.account.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    position = serializers.CharField()

    class Meta:
        model = Profile
        fields = [
            "avatar",
            "position",
        ]
        ref_name = 'board_profile'


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name", 
            "profile"
        ]
        ref_name = 'board_user'

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payment
        fields = [
            "id",
            "user",
            "idea"
        ]


class LocationSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = models.Idea
        fields = [
            "id",
            "name"
        ]
        ref_name = 'board_category'


class IdeaListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    # file = FileSerializer()
    category = CategorySerializer()

    class Meta:
        model = models.Idea
        fields = [
            "id",
            "user",
            "category",
            "name",
            "created",
            "description",
            "likes",
            "user_likes",
            "status",
            # "file",
        ]
