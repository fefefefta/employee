from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    """Мероприятие"""
    name = models.CharField(max_length=50)
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.TextField()
    payment = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.name


class Idea(models.Model):
    """Идея от пользователя"""
    name = models.CharField(max_length=100)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    user_likes = models.ManyToManyField(
        User,
        related_name='likes_user_ideas',
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']


class Payment(models.Model):
    """Оплата за идею"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    payment = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    idea = models.ForeignKey(
        Idea,
        on_delete=models.CASCADE,
        related_name='+'
    )

    def __str__(self):
        return self.idea.name


class Location(models.Model):
    """Адрес мероприятия"""
    city = models.CharField(max_length=20)
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='+',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.city


class Image(models.Model):
    """Изображения для мероприятия"""
    image = models.ImageField(upload_to="event/image/")
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='+'
    )

    def __str__(self):
        return self.event.name
