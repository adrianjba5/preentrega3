from django.urls import path
from apppreentrega.views import *

urlpatterns = [
    path("", inicio),
    path("/crear-cliente",crear_cliente),
    path("/mostrar-clientes",mostrar_clientes),
    
]
