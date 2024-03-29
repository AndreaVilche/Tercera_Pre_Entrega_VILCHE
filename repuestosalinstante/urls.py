from django.urls import path, include
from django.contrib.auth.views import LogoutView

from .views import *
urlpatterns = [
    path('', home, name='home'),

    #MAS PAGINAS
    path('acerca/', acerca, name="acerca_de"),

    #__________productos
    path('productos/', productos, name='productos'),
    path('producto_create/', productoCreate, name="producto_create"),
    path('producto_update/<id_producto>/', productoUpdate, name="producto_update"),
    path('producto_delete/<id_producto>/', productoDelete, name="producto_delete"),
    
    #_______categorias de productos
    path('categorias/', CategoriaList.as_view(), name="categorias"),
    path('create_categoria/', CategoriaCreate.as_view(), name="create_categoria" ),    
    path('update_categoria/<int:pk>/', CategoriaUpdate.as_view(), name="update_categoria" ),
    path('delete_categoria/<int:pk>/', CategoriaDelete.as_view(), name="delete_categoria" ),


    #________clientes
    path('clientes/', clientes, name='clientes'),
    path('cliente_create/', clienteCreate, name="cliente_create"),
    path('cliente_update/<id_cliente>/', clienteUpdate, name="cliente_update"),
    path('cliente_delete/<id_cliente>/', clienteDelete, name="cliente_delete"),

    #___________marcas
    path('marcas/', MarcaList.as_view(), name="marcas"),
    path('create_marca/', MarcaCreate.as_view(), name="create_marca" ),    
    path('update_marca/<int:pk>/', MarcaUpdate.as_view(), name="update_marca" ),
    path('delete_marca/<int:pk>/', MarcaDelete.as_view(), name="delete_marca" ),
    
    #BUSCAR
    path('buscar_productos/', buscarProductos, name="buscar_productos"),
    path('encontrar_productos/', encontrarProductos, name="encontrar_productos"),

    #_________LOGIN, LOGOUT, REGIST
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="repuestosalinstante/logout.html") , name="logout"),
    path('registrar/', register, name="registrar"),


    #____________________ EDICION DE PERFIL
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiar_clave"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),

]
