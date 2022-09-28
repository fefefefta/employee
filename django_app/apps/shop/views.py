from rest_framework.viewsets import ModelViewSet

from ..base.permissions import IsAuthor
from .models import Product, Comment
from .serializers import ProductDetailSerializer, ProductListSerializer, \
    CommentSerializer, CommentAuthorSerializer


class ProductListView(ModelViewSet):
    """Список товаров"""
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailView(ModelViewSet):
    """Продукт детально"""
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class CommentView(ModelViewSet):
    """Комментарий к товару"""
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(product_id=self.kwargs.get("pk"))


class CommentAuthorView(ModelViewSet):
    """CRUD комментариев автора"""
    serializer_class = CommentAuthorSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
