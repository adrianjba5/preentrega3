from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def crear_cliente(request):
#     nombre = input("Ingrese su nombre" )
#     apellido = input("Ingrese su apellido" )
#     correo = input("Ingrese su correo" )
#     cliente = Client(nombre=nombre, apellido=apellido, correo=correo)
#     cliente.save()
#     texto = f"Cliente registrado con exito."
#     return HttpResponse(texto)

# def mostrar_clientes(request):
#     clientes = Client.objects.all()
#     contexto = {"Client": clientes}
#     return render(request, "clientes.html", contexto)

def inicio(request):
    return render(request, "apppreentrega/inicio.html")

def crear_cliente(request):
    return render(request, "apppreentrega/nosotros.html")

def mostrar_clientes(request):
    return HttpResponse("Esta vista para Mostrar cliente")
    