from django.urls import path
from . import views

urlpatterns = [
    path('bosses', views.bosses),
    path('bosses2', views.bosses2),
]
