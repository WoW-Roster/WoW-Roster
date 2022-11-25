from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.add_character),
    path('', views.list_characters),
]
