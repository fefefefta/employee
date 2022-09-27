from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    """Тэг"""
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Category(models.Model):
    """Категория"""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Товар"""
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    tags = models.ManyToManyField(
        Tag,
        blank=True
    )

    def __str__(self):
        return self.name


class Image(models.Model):
    """Изображение для товара"""
    image = models.ImageField(upload_to="product/image/")
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='+'
    )

    def __str__(self):
        return self.product.name


class Comment(models.Model):
    """Комментарий товара"""
    product = models.ForeignKey(
        Product,
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
        return self.product.name, self.user.username

    class Meta:
        ordering = ['created']
