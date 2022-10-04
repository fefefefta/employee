from rest_framework.viewsets import ModelViewSet

from .models import Product, Cart, CartItem, Order, OrderItem
from .serializers import ProductSerializer, CartItemSerializer, \
    OrderSerializer, OrderItemSerializer


class ProductView(ModelViewSet):
    """Список товаров"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartView(ModelViewSet):
    """Корзина"""
    serializer_class = CartItemSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = CartItem.objects.filter(cart=user.cart)
        return queryset

    def perform_create(self, serializer):
        try:
            cart_item = CartItem.objects.get(
                cart=self.request.user.cart,
                product=serializer.validated_data["product"]
            )
        except CartItem.DoesNotExist:            
            serializer.save(cart=self.request.user.cart)
        else:
            cart_item.quantity += serializer.validated_data["quantity"]
            cart_item.save()


class OrderView(ModelViewSet):
    """Заказ"""
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Order.objects.filter(user=user)
        return queryset

    def perform_create(self, serializer):
        order = serializer.save(
            user=self.request.user
        )

        cart = Cart.objects.get(user=self.request.user)
        for item in cart.items.all():
            order_item = OrderItem(
                order=order,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity
            )
            order_item.save()
        cart.clear()
