from rest_framework.viewsets import ModelViewSet

from ..base.permissions import IsAuthor
from .models import Post, Comment
from .serializers import CategorySerializer, PostListSerializer, \
    PostDetailSerializer, PostAuthorSerializer, CategoryPostView, \
    CommentSerializer, CommentAuthorSerializer


class PostListView(ModelViewSet):
    """Список постов"""
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostDetailView(ModelViewSet):
    """Пост детально"""
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostAuthorView(ModelViewSet):
    """CRUD постов автора"""
    serializer_class = PostAuthorSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryPostView(ModelViewSet):
    """Посты в категории"""
    serializer_class = CategoryPostView

    def get_queryset(self):
        return Post.objects.filter(category_id=self.kwargs.get('pk'))


class CommentAuthorView(ModelViewSet):
    """CRUD комментариев автора"""
    serializer_class = CommentAuthorSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentView(ModelViewSet):
    """Комментарии к посту"""
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs.get("pk"))
