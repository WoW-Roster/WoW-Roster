from django.urls import path
from . import views

urlpatterns = [
    path("players_selection", views.BossListView.as_view(), name="boss_list_view"),
    path("boss_update/<int:pk>/", views.BossUpdateView.as_view(), name="boss_update"),
]
