from django.contrib.auth.models import User
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Departament(models.Model):
    """Отдел банка"""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Profile(models.Model):
    """Профиль пользователя"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    avatar = models.ImageField(upload_to="profile/avatar/", blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone = PhoneNumberField(null=True, blank=True, unique=True, region="RU")
    departament = models.ForeignKey(
        Departament,
        on_delete=models.CASCADE,
        related_name='+',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username


class Location(models.Model):
    """Адрес"""
    city = models.CharField(max_length=20)
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        related_name='+',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.city


class Wallet(models.Model):
    """Кошелек"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    balance = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.user.username
