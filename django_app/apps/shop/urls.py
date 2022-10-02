from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'cart', views.CartView, basename='Cart')

urlpatterns = [
    path('', include(router.urls)),
    path('products/', views.ProductView.as_view({'get': 'list'})),
]
