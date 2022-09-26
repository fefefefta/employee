from django.contrib.auth.models import User
from django.db import models



class Tag(models.Model):
    name = models.CharField(max_length=15)


class Category(models.Model):
    name = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)
    categories = models.ManyToManyField(Category)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    status = models.BooleanField(default=True)


class Image(models.Model):
    image = models.ImageField(upload_to="product/image/")
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='+'
    )


class Comment(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    text = models.TextField()
    status = models.BooleanField(default=True)
