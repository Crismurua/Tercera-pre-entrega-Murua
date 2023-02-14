from django.urls import path

from app import views



urlpatterns = [
   
    path('', views.home, name="Home"), #esta era nuestra primer view
    path('productos', views.productos, name="Productos"),
    path('vendedores', views.vendedores, name="Vendedores"),
    path('compradores', views.compradores, name="Compradores"),
    path('ofertas', views.ofertas, name="Ofertas"),
    #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    #path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    #path('busquedaCamada',  views.busquedaCamada, name="BusquedaCamada"),
    # path('buscar/', views.buscar),
   
]