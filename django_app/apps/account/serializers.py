from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile, Achievement, Wallet, Location
from ..board.models import Payment


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = [
            "id",
            "balance"
        ]


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment.objects.all()
        fields = [
            "idea",
            "payment"
        ]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location.objects.all()
        fields = [
            "city",
        ]


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = [
            "id",
            "icon",
            "name",
            "description"
        ]


class ProfileSerializer(serializers.ModelSerializer):
    position = serializers.CharField()
    # location = LocationSerializer()

    class Meta:
        model = Profile
        fields = [
            "avatar",
            "birthday",
            "bio",
            "phone",
            "position",
            "departament",
            "achievements",
            # "location",
        ]
        ref_name = 'account_profile'


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    wallet = WalletSerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "profile",
            "wallet",

        ]
        ref_name = 'account_user'

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user
