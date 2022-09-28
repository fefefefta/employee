from .models import Tag, Product, Comment, Category, Image

from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    """Категории"""

    class Meta:
        model = Category
        fields = [
            "id",
            "name"
        ]


class ImageSerializer(serializers.ModelSerializer):
    """Изображения для товара"""

    class Meta:
        model = Image
        fields = [
            "image",
        ]


class TagSerializer(serializers.ModelSerializer):
    """Тэг товара"""

    class Meta:
        model = Tag
        fields = [
            "id",
            "name"
        ]


class CommentAuthorSerializer(serializers.ModelSerializer):
    """Комментарий"""

    class Meta:
        model = Comment
        fields = [
            'id',
            'text',
            'product'
        ]


class CommentSerializer(serializers.ModelSerializer):
    """Комментарий"""

    class Meta:
        model = Comment
        fields = [
            "id",
            "product",
            "user",
            "text",
            "created"
        ]


class ProductListSerializer(serializers.ModelSerializer):
    """Список товаров"""
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "category",
            "tags"
        ]


class ProductDetailSerializer(serializers.ModelSerializer):
    """Товар детально"""
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    product_images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "category",
            "tags",
            "product_images",
        ]
