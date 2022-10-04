from django.urls import path

from . import views

urlpatterns = [
    path('events/', views.EventListView.as_view()),
    path('event/<int:id>/', views.EventDetailView.as_view()),
    path('ideas/', views.IdeaListView.as_view({'get': 'list'})),
    path('create-idea/', views.IdeaCreateView.as_view({'post': 'create'})),
]
