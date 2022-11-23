from django.urls import path
from . import views

urlpatterns = [
    path('Bosses', views.Bosses),
]