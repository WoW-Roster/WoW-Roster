from django.urls import path
from . import views

urlpatterns = [
    path('roster/bosses_selection', views.bosses_selection),
    path('roster/players_selection', views.players_selection),
]
