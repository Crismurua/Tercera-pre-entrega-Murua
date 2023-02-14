from django.urls import path

from .views import *



urlpatterns = [
   
    path('', home, name="Home"),
    path('productos', productos, name="Productos"),
    path('vendedores', vendedores, name="Vendedores"),
    path('compradores', compradores, name="Compradores"),
    path('ofertas', ofertas, name="Ofertas"),
    path('buscar/', buscar),
   
]