from django.contrib.auth.models import User
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from apps.board.models import Departament


class Achievement(models.Model):
    """Достижения"""
    icon = models.ImageField('иконка', upload_to='achievements/')
    name = models.CharField("название", max_length=50)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "достижение"
        verbose_name_plural = "достижения"

    def __str__(self):
        return self.name


class Position(models.Model):
    """Должность"""
    name = models.CharField("название должности", max_length=25)

    class Meta:
        verbose_name = "должность",
        verbose_name_plural = "должности"

    def __str__(self):
        return self.name


class Profile(models.Model):
    """Профиль пользователя"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='пользователь'
    )
    avatar = models.ImageField(
        upload_to="profile/avatar/",
        verbose_name='Аватар',
        blank=True,
        null=True
    )
    birthday = models.DateField('дата рождения', blank=True, null=True)
    bio = models.TextField('о себе', blank=True, null=True)
    phone = PhoneNumberField('номер телефона', null=True, blank=True, unique=True, region="RU")
    departament = models.ForeignKey(
        Departament,
        on_delete=models.CASCADE,
        related_name='+',
        verbose_name='отдел',
        blank=True,
        null=True
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        verbose_name='должность',
        blank=True,
        null=True
    )
    achievements = models.ManyToManyField(
        Achievement,
        blank=True,
        verbose_name='достижения'
    )

    class Meta:
        verbose_name = "профиль"
        verbose_name_plural = "профили"

    def __str__(self):
        return self.user.username


class Location(models.Model):
    """Адрес"""
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        related_name='+',
        verbose_name='адрес',
        blank=True,
        null=True
    )
    city = models.CharField('город', max_length=20)

    class Meta:
        verbose_name = 'адрес'
        verbose_name_plural = 'адреса'

    def __str__(self):
        return self.city


# Добавить токены
class Wallet(models.Model):
    """Кошелек"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='пользователь',
    )
    balance = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
        verbose_name='баланс'
    )

    class Meta:
        verbose_name = "кошелек"
        verbose_name_plural = "кошельки"

    def __str__(self):
        return f'{self.user.username}'
