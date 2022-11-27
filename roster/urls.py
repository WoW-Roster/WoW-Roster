from django.urls import path
from . import views

urlpatterns = [
    path('bosses_selection', views.bosses_selection),
    # path('players_selection', views.players_selection),
    path('players_selection', views.BossListView.as_view()),
]
