from django.urls import path

from .views import PostListView, PostDetailView, PostAuthorView, \
    CategoryPostView, CommentAuthorView, CommentView

urlpatterns = [
    path('post/', PostListView.as_view({'get': 'list'})),
    path('post/<int:pk>/', PostDetailView.as_view({'get': 'retrieve'})),

    path('user-post/', PostAuthorView.as_view({'get': 'list', 'post': 'create'})),
    path('user-post/<int:pk>/', PostAuthorView.as_view({'put': 'update', 'delete': 'destroy'})),

    path('comments/', CommentAuthorView.as_view({'get': 'list', 'post': 'create'})),
    path('comments/<int:pk>/', CommentAuthorView.as_view({'put': 'update', 'delete': 'destroy'})),

    path('category/<int:pk>/', CategoryPostView.as_view({'get': 'list'})),

    path('post-comment/<int:pk>', CommentView.as_view({'get': 'list'})),
]
