from django.urls import path

from .views import *



urlpatterns = [
   
    path('', home, name="Home"),
    path('productos', productos, name="Productos"),
    path('vendedores', vendedores, name="Vendedores"),
    path('compradores', compradores, name="Compradores"),
    path('ofertas', ofertas, name="Ofertas"),
    #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    #path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    #path('busquedaCamada',  views.busquedaCamada, name="BusquedaCamada"),
    # path('buscar/', views.buscar),
   
]