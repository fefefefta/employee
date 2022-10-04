from django.urls import path

from .views import UserViewSet

urlpatterns = [
    path("users/", UserViewSet.as_view({"get": "list"})),
    path("user/<int:pk>/", UserViewSet.as_view({"get": "retrieve"}))
]
