from .models import Category, Post, Comment

from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    """Категории"""

    class Meta:
        model = Category
        fields = [
            "id",
            "name"
        ]


class PostListSerializer(serializers.ModelSerializer):
    """Список постов"""

    category = CategorySerializer()

    class Meta:
        model = Post
        fields = [
            "id",
            "user",
            "name",
            "category",
        ]


class PostDetailSerializer(serializers.ModelSerializer):
    """Пост детально"""

    category = CategorySerializer()

    class Meta:
        model = Post
        fields = [
            "id",
            "user",
            "name",
            "category",
            "description",
        ]


class PostAuthorSerializer(serializers.ModelSerializer):
    """Пост автора"""

    class Meta:
        model = Post
        fields = [
            'id',
            'name',
            'description',
            'category',
        ]


class CategoryPostView(serializers.ModelSerializer):
    """Посты в категории"""

    class Meta:
        model = Post
        fields = [
            "id",
            "user",
            "name",
            "created"
        ]


class CommentSerializer(serializers.ModelSerializer):
    """Комментарии к посту"""

    class Meta:
        model = Comment
        fields = [
            "id",
            "post",
            "user",
            "text",
            "created"
        ]


class CommentAuthorSerializer(serializers.ModelSerializer):
    """Комментарий"""

    class Meta:
        model = Comment
        fields = [
            'id',
            'text',
            'post'
        ]
