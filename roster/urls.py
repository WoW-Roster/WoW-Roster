from django.urls import path
from . import views

urlpatterns = [
    path('bosses', views.bosses),
]
