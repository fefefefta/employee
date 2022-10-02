from rest_framework.viewsets import ModelViewSet

from .models import Product, Cart
from .serializers import ProductSerializer, CartSerializer


class ProductView(ModelViewSet):
    """Список товаров"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartView(ModelViewSet):
    """Корзина"""
    serializer_class = CartSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Cart.objects.filter(id=user.id)
        return queryset


class OrderView(ModelViewSet):
    """Заказ"""
    pass
