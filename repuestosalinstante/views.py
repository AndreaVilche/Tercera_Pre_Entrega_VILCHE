from django.shortcuts import render
##from django.http import HttpResponse
from .models import *
from .forms import *

def home(request):
    return render(request, "repuestosalinstante/index.html")

def clientes(request):
    contexto ={'clientes': Cliente.objects.all()} 
    return render(request, 'repuestosalinstante/clientes.html', contexto)

def productos(request):
    productos = Producto.objects.all()
    return render(request, "repuestosalinstante/productos.html", {"productos": productos})

def marcas(request):
    marcas = Marca.objects.all()
    return render(request, "repuestosalinstante/marcas.html", {"marcas": marcas})


def acerca(request):
    return render(request, "repuestosalinstante/acerca.html") 

#FORMULARIOS
def productoForm(request):
    
    if request.method == "POST":
        miForm = ProductoForm(request.POST)
        if miForm.is_valid():
            producto_nombre = miForm.cleaned_data.get("nombre")
            producto_marca = miForm.cleaned_data.get("marca")
            producto_precio = miForm.cleaned_data.get("precio")
            producto = Producto(nombre=producto_nombre, precio=producto_precio, marca=producto_marca)
            producto.save()

            contexto = {'productos': Producto.objects.all()}
            return render(request, "repuestosalinstante/productos.html", contexto) 

    else:

        miForm = ProductoForm()

    return render(request, "repuestosalinstante/productoForm.html", {"form": miForm} )

def clienteForm(request):

    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente_nombre = miForm.cleaned_data.get("nombre")
            cliente_direccion = miForm.cleaned_data.get("direccion")
            cliente_telefono = miForm.cleaned_data.get("telefono")

            cliente = Cliente(nombre=cliente_nombre, 
                             direccion=cliente_direccion,
                             telefono=cliente_telefono,
                             )
            cliente.save()
            
            contexto = {'clientes': Cliente.objects.all()}
            return render(request, "repuestosalinstante/clientes.html", contexto) 

    else:
        miForm = ClienteForm()

    return render(request, "repuestosalinstante/clienteForm.html", {"form": miForm} )

def marcaForm(request):

    if request.method == "POST":
        miForm = MarcaForm(request.POST)
        if miForm.is_valid():
            marca_nombre = miForm.cleaned_data.get("nombre")
            marca_pais = miForm.cleaned_data.get("pais_origen")
            
            marca = Marca(nombre=marca_nombre, 
                             pais_origen=marca_pais,
                             )
            marca.save()
            
            contexto = {'marcas': Marca.objects.all()}
            return render(request, "repuestosalinstante/marcas.html", contexto) 

    else:
        miForm = MarcaForm()

    return render(request, "repuestosalinstante/marcaForm.html", {"form": miForm} )

#________________________ Buscar

def buscarProductos(request):
    return render(request, "repuestosalinstante/buscar.html")

def encontrarProductos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        productos = Producto.objects.filter(nombre__icontains=patron)
        contexto = {"productos": productos}
        return render(request, "repuestosalinstante/productos.html", contexto)
    

    contexto = {'productos': Producto.objects.all()}
    return render(request, "repuestosalinstante/productos.html", contexto) 