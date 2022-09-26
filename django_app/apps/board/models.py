from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=50)
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.TextField()
    payment = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.name


class Idea(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']


class Payment(models.Model):
    payment = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    idea = models.ForeignKey(
        Idea,
        on_delete=models.CASCADE,
        related_name='+'
    )

    def __str__(self):
        return self.idea.name


class Location(models.Model):
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
    image = models.ImageField(upload_to="event/image/")
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='+'
    )

    def __str__(self):
        return self.event.name
