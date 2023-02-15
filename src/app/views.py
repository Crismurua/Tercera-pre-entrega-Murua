from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from app.models import *
from app.forms import *

# Create your views here.
def home(request):

      return render(request, "app/home.html")


def vendedores(request):

      vendedores = Vendedor.objects.all()

      if request.method == 'POST':

            formulario = VendedorFormulario(request.POST) 

            if formulario.is_valid():

                  informacion = formulario.cleaned_data

                  vendedor = Vendedor (nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], ventas=informacion['ventas']) 

                  vendedor.save()
                  formulario = VendedorFormulario()
                  return render(request, "app/vendedores.html", {"formulario":formulario, "vendedores":vendedores})

      else: 

            formulario= VendedorFormulario() #Formulario vacio para construir el html

      return render(request, "app/vendedores.html", {"formulario":formulario, "vendedores":vendedores})


def compradores(request):
      
      compradores = Comprador.objects.all()

      if request.method == 'POST':

            formulario = CompradorFormulario(request.POST) 

            if formulario.is_valid():

                  informacion = formulario.cleaned_data

                  comprador = Comprador (nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], compras=informacion['compras']) 

                  comprador.save()
                  
                  formulario = CompradorFormulario()
                  
                  return render(request, "app/compradores.html", {"formulario":formulario, "compradores":compradores})

      else: 

            formulario= CompradorFormulario() #Formulario vacio para construir el html

      return render(request, "app/compradores.html", {"formulario":formulario, "compradores":compradores})

      
  

def ofertas(request):
    
      ofertas = Oferta.objects.all()

      if request.method == 'POST':

            formulario = OfertaFormulario(request.POST) 

            if formulario.is_valid():

                  informacion = formulario.cleaned_data

                  oferta = Oferta (producto=informacion['producto'], cantidad=informacion['cantidad'], total=informacion['total']) 

                  oferta.save()

                  formulario= OfertaFormulario()
                  
                  return render(request, "app/ofertas.html", {"formulario":formulario, "ofertas":ofertas})

      else: 

            formulario= OfertaFormulario() #Formulario vacio para construir el html

      return render(request, "app/ofertas.html", {"formulario":formulario, "ofertas":ofertas})


def productos(request):
      productos = Producto.objects.all()

      if request.method == 'POST':

            formulario = ProductoFormulario(request.POST) 

            if formulario.is_valid():

                  informacion = formulario.cleaned_data

                  producto = Producto (nombre=informacion['nombre'], cantidad=informacion['cantidad'], precio=informacion['precio']) 

                  producto.save()
                  
                  formulario= ProductoFormulario()

                  return render(request, "app/productos.html", {"formulario":formulario, "productos":productos})

      else: 

            formulario= ProductoFormulario() #Formulario vacio para construir el html

      return render(request, "app/productos.html", {"formulario":formulario, "productos":productos})


def buscar(request):
      
      if  request.GET["nombre"]:

            nombre = request.GET['nombre'] 
            productos = Producto.objects.filter(nombre__icontains=nombre)

            return render(request, "app/home.html", {"productos":productos})

      else: 
            respuesta = "Producto no encontrado"

      return render(request, "app/home.html", {"respuesta":respuesta, "productos":productos})


def buscar_oferta(request):
      
      if  request.GET["producto"]:

            producto = request.GET['producto'] 
            ofertas = Oferta.objects.filter(producto__icontains=producto)

            return render(request, "app/home.html", {"ofertas":ofertas})

      else: 
            respuesta = "Oferta no encontrado"

      return render(request, "app/home.html", {"respuesta":respuesta, "ofertas":ofertas})


def buscar_vendedor(request):
      
      if  request.GET["email"]:

            email = request.GET['email'] 
            vendedores = Vendedor.objects.filter(email__icontains=email)

            return render(request, "app/home.html", {"vendedores":vendedores})

      else: 
            respuesta = "Vendedor no encontrado"

      return render(request, "app/home.html", {"respuesta":respuesta, "vendedores":vendedores})


def buscar_comprador(request):
      
      if  request.GET["email"]:

            email = request.GET['email'] 
            compradores = Comprador.objects.filter(email__icontains=email)

            return render(request, "app/home.html", {"compradores":compradores})

      else: 
            respuesta = "Comprador no encontrado"

      return render(request, "app/home.html", {"respuesta":respuesta, "compradores":compradores})