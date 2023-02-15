from django.urls import path

from .views import *



urlpatterns = [
   
    path('', home, name="home"),
    path('productos/', productos, name="productos"),
    path('vendedores/', vendedores, name="vendedores"),
    path('compradores/', compradores, name="compradores"),
    path('ofertas/', ofertas, name="ofertas"),
    path('buscar/', buscar, name='buscar'),
    path('buscar-oferta/', buscar_oferta, name='buscar_oferta'),
    path('buscar-vendedor/', buscar_vendedor, name='buscar_vendedor'),
    path('buscar-comprador/', buscar_comprador, name='buscar_comprador'),
   
]