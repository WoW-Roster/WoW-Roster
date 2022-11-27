from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.add_character),
    path('delete/', views.delete_character),
    path('change_role/', views.change_character_role),
    path('', views.list_characters),
]
