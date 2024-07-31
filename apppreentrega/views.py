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
    return render(request, "apppreentrega/crear-cliente.html")

def mostrar_clientes(request):
    return render(request, "apppreentrega/mostrar.html")


from apppreentrega.models import Client


def crear_cliente(request):
    
    if request.method == 'POST':
        
        cliente =Client(nombre=request.POST['nombre'],apellido=request.POST['apellido'],correo=request.POST['correo'])
        cliente.save()
        
        return render(request, "apppreentrega/crear-cliente.html")
    
    return render(request,"apppreentrega/crear-cliente.html")

def mostrar(request):
    
    return render(request, "apppreentrega/mostrar")

def buscar(request):
    
    if request.GET["nombre"]:
        cliente = request.Get['nombre']
        cliente = Client.objects.filter(cliente__icontains=nombre)
    
        return render(request, "apppreentrega/mostrar.html", {"nombre":nombre, "apellido":apellido,"correo":correo})

    else:
    
        respuesta = " No enviaste Datos"
        
    return HttpResponse(respuesta)