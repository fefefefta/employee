from rest_framework import serializers

from .models import Product, Category, Cart


class CategorySerializer(serializers.ModelSerializer):
    """Категории"""

    class Meta:
        model = Category
        fields = [
            "id",
            "name"
        ]
        ref_name = "shop_category"


class ProductSerializer(serializers.ModelSerializer):
    """Список товаров"""
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "category",
            "image",
        ]


class CartSerializer(serializers.ModelSerializer):
    """Товары в корзине"""
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = [
            'id',
            'product',
        ]
