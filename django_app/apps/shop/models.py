from django.contrib.auth.models import User
from django.db import models



class Tag(models.Model):
    name = models.CharField()


class Category(models.Model):
    name = models.CharField()


class Product(models.Model):
    tags = models.ManyToManyField(Tag)
    categories = models.ManyToManyField(Category)
    name = models.CharField()
    description = models.TextField()
    price = models.DecimalField()
    status = models.BooleanField(default=True)


class Image(models.Model):
    path = models.CharField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    status = models.BooleanField(default=True)
