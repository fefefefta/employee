from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Категория"""
    name = models.CharField("название", max_length=50, unique=True)

    class Meta:
        verbose_name = "категорию"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    """Товар"""
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='категория'
    )
    name = models.CharField("название", max_length=50)
    image = models.ImageField("изображение", upload_to="product/image/", blank=True, null=True)
    description = models.TextField("описание", blank=True, null=True)
    price = models.DecimalField("цена", max_digits=8, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def __str__(self):
        return self.name


class Cart(models.Model):
    """Корзина пользователя"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='пользователь',
    )
    product = models.ManyToManyField(
        Product,
        blank=True,
        verbose_name='товар'
    )

    class Meta:
        verbose_name = "корзину"
        verbose_name_plural = "корзины"

    def __str__(self):
        return self.user.username
