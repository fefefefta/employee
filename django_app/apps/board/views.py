from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import OrderingFilter

from .models import Event, Idea
from .serializers import (
    EventListSerializer,
    EventDetailSerializer,
    IdeaListSerializer
)


class EventListView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer


class EventDetailView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer


class IdeaListView(ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaListSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['category', ]
    ordering_fields = ['likes', 'created', ]


class IdeaCreateView(ModelViewSet):
    # parser_classes = (MultiPartParser,)

    serializer_class = IdeaListSerializer

    def get_queryset(self):
        return Idea.objects.filter(user=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.id)
