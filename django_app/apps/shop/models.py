from django.contrib.auth.models import User
from django.db import models



class Tag(models.Model):
    name = models.TextField()


class Category(models.Model):
    name = models.TextField()


class Product(models.Model):
    tags = models.ManyToManyField(Tag)
    categories = models.ManyToManyField(Category)
    name = models.TextField()
    description = models.TextField()
    price = models.TextField()
    status = models.TextField()


class Image(models.Model):
    path = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    status = models.TextField()
