from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import parsers
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers
from .models import Idea


# Список категорий
class EventListView(ListAPIView):
    """Список событий"""
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventListSerializer
    # pagination_class = 9


class EventDetailView(RetrieveAPIView):
    """Событие подробно"""
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventDetailSerializer


class IdeaListView(ModelViewSet):
    """Список идей"""
    queryset = Idea.objects.all()
    serializer_class = serializers.IdeaListSerializer
    # pagination_class = 4
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['category', ]
    ordering_fields = ['likes', 'created', ]


class IdeaCreateView(ModelViewSet):
    """Создание идеи"""
    parser_classes = (parsers.MultiPartParser,)
    serializer_class = serializers.IdeaListSerializer

    def get_queryset(self):
        return models.Idea.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
