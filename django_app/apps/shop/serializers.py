from rest_framework import serializers

from .models import Product, Category, Cart, CartItem, Order, OrderItem


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


class CartItemSerializer(serializers.ModelSerializer):
    """Товар в корзине"""

    class Meta:
        model = CartItem
        fields = [
            'id',
            'product',
            'quantity'
        ]


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            'id',
            'product',
            'price',
            'quantity'
        ]


class OrderSerializer(serializers.ModelSerializer):
    """Заказ"""
    total_cost = serializers.ReadOnlyField()
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'address',
            'postal_code',
            'city',
            'total_cost',
            'items',
            'created',
        ]


class CartItemSerializer(serializers.ModelSerializer):
    """Товар в корзине"""

    class Meta:
        model = CartItem
        fields = [
            'id',
            'product',
            'quantity'
        ]