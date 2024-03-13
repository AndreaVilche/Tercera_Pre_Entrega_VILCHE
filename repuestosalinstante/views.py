from django.shortcuts import render

from .models import *

def home(request):
    return render(request, "repuestosalinstante/index.html")

def clientes(request):
    contexto ={'clientes': Cliente.objects.all()} 
    return render(request, 'repuestosalinstante/clientes.html', contexto)

def productos(request):
    productos = Producto.objects.all()
    return render(request, "repuestosalinstante/productos.html", {"productos": productos})

def detalle_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, "repuestosalinstante/detalle_producto.html", {"producto": producto})

def marcas(request):
    marcas = Marca.objects.all()
    return render(request, "repuestosalinstante/marcas.html", {"marcas": marcas})

def detalle_marca(request, marca_id):
    marca = Marca.objects.get(id=marca_id)
    return render(request, "repuestosalinstante/detalle_marca.html", {"marca": marca})

def categorias(request):
    categorias = CategoriaProducto.objects.all()
    return render(request, "repuestosalinstante/categorias.html", {"categorias": categorias})

def detalle_categoria(request, categoria_id):
    categoria = CategoriaProducto.objects.get(id=categoria_id)
    return render(request, "repuestosalinstante/detalle_categoria.html", {"categoria": categoria})
