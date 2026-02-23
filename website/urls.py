from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('trabalhos/', views.trabalhos, name='trabalhos'),
    path('contato/', views.contato, name='contato'),
    path('reservar/', views.reservar, name='reservar'),
]
