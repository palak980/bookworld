from django.urls import path
from .import views

urlpatterns = [
    path('searchapi/', views.Searchlist.as_view()),
    path('api/', views.location.as_view()),
]
