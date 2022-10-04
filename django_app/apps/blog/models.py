from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    """Категория"""
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name


class Post(models.Model):
    """Публикации"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='+'
    )
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='+',
        verbose_name='категория'
    )
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "публикации"

    def __str__(self):
        return self.name


class Comment(models.Model):
    """Комментарии"""
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='+'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='+'
    )
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['created']
        verbose_name = "комментарий"
        verbose_name_plural = "комментарии"
