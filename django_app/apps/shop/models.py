from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    """Тэг"""
    name = models.CharField("тэг", max_length=15)

    class Meta:
        verbose_name = "тэг"
        verbose_name_plural = "тэги"

    def __str__(self):
        return self.name


class Category(models.Model):
    """Категория"""
    name = models.CharField("название", max_length=50)

    class Meta:
        verbose_name = "категорию"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    """Товар"""
    name = models.CharField("название", max_length=50)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=8, decimal_places=2, default=0)
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        verbose_name="тэги"
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def __str__(self):
        return self.name


class Image(models.Model):
    """Изображение для товара"""
    image = models.ImageField("изображение", upload_to="product/image/")
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='+',
        verbose_name="товар",
    )

    class Meta:
        verbose_name = "изображение"
        verbose_name_plural = "изображения"

    def __str__(self):
        return self.product.name


class Comment(models.Model):
    """Комментарий товара"""
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='+',
        verbose_name="товар",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='+',
        verbose_name="пользователь"
    )
    text = models.TextField("текст")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        verbose_name = "комментарий"
        verbose_name_plural = "комментарии"

    def __str__(self):
        return self.product.name, self.user.username
