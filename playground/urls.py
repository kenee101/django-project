from django.urls import path
from . import views

#URLConfig
urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
]
