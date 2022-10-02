from django.urls import path

from . import views

urlpatterns = [
    path('events/', views.EventListView.as_view()),
    path('events/<int:id>/', views.EventDetailView.as_view()),
    path('ideas/', views.IdeaListView.as_view({'get': 'list'})),
    path('my-idea/', views.IdeaCreateView.as_view({'post': 'create'})),
]
