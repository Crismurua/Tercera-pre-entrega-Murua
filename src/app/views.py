from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from app.models import *
from app.forms import *

# Create your views here.
def home(request):

      return render(request, "app/home.html")


def vendedores(request):

      return render(request, "app/vendedores.html")


def compradores(request):

      return render(request, "app/compradores.html")
  

def ofertas(request):
    
    return render(request, 'app/ofertas.html')

def productos(request):

      if request.method == 'POST':

            formulario = ProductoFormulario(request.POST) 

            if formulario.is_valid():

                  informacion = formulario.cleaned_data

                  producto = Producto (nombre=informacion['nombre'], cantidad=informacion['cantidad'], precio=informacion['precio']) 

                  producto.save()

                  return render(request, "app/home.html")

      else: 

            formulario= ProductoFormulario() #Formulario vacio para construir el html

      return render(request, "app/productos.html", {"formulario":formulario})


def buscar(request):

      if  request.GET["nombre"]:

            nombre = request.GET['nombre'] 
            precio = Producto.objects.filter(nombre__icontains=nombre)

            return render(request, "app/home.html", {"nombre":nombre, "precio":precio})

      else: 
            respuesta = "No enviaste datos"

      return render(request, "app/home.html", {"respuesta":respuesta})