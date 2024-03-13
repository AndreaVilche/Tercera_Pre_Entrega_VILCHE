from django.urls import path, include
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('productos/', productos, name='productos'),
    path('categorias/', categorias, name='categorias'),
    path('marcas/', marcas, name='marcas'),
    path('clientes/', clientes, name='clientes'),
]
