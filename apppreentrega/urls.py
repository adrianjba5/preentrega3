from django.urls import path
from apppreentrega.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("crear-cliente",crear_cliente, name="crear"),
    path("mostrar",mostrar_clientes, name="mostrar"),
    path("mostrar", views.buscar),
    
]
