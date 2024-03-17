from django.urls import path, include
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('productos/', productos, name='productos'),
    path('marcas/', marcas, name='marcas'),
    path('clientes/', clientes, name='clientes'),

    #MAS PAGINAS
    path('acerca/', acerca, name="acerca_de"),

    #FORMULARIOS
    path('producto_form/', productoForm, name="producto_form"),
    path('cliente_form/', clienteForm, name="cliente_form"),
    path('marca_form/', marcaForm, name="marca_form"),

    #BUSCAR
    path('buscar_productos/', buscarProductos, name="buscar_productos"),
    path('encontrar_productos/', encontrarProductos, name="encontrar_productos"),
]
