from django.urls import path

from .views import ProductListView, ProductDetailView, CommentView, CommentAuthorView

urlpatterns = [
    path('product/', ProductListView.as_view({'get': 'list'})),
    path('product/<int:pk>/', ProductDetailView.as_view({'get': 'retrieve'})),

    path('comments/', CommentAuthorView.as_view({'get': 'list', 'post': 'create'})),
    path('comments/<int:pk>/', CommentAuthorView.as_view({'put': 'update', 'delete': 'destroy'})),

    path('product-comment/<int:pk>', CommentView.as_view({'get': 'list'})),
]
