from django.urls import path

from . import views

app_name = "characters"

urlpatterns = [
    path("add/", views.add_character, name="add_character"),
    path("delete/", views.delete_character, name="delete_character"),
    path("change_role/", views.change_character_role, name="change_character_role"),
    path("", views.list_characters, name="list_characters"),
]
