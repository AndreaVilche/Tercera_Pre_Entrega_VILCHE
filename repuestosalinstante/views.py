from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy



from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

def home(request):
    return render(request, "repuestosalinstante/index.html")

#_________________ADICIONALES

def acerca(request):
    return render(request, "repuestosalinstante/acerca.html") 

#__________________PRODUCTOS
@login_required
def productos(request):
    contexto ={'productos': Producto.objects.all().order_by('nombre')} 
    return render(request, 'repuestosalinstante/productos.html', contexto)

@login_required
def productoCreate(request):
    
    if request.method == "POST":
        miForm = ProductoForm(request.POST)
        if miForm.is_valid():
            producto_nombre = miForm.cleaned_data.get("nombre")
            producto_marca = miForm.cleaned_data.get("marca")
            producto_precio = miForm.cleaned_data.get("precio")
            producto = Producto(nombre=producto_nombre, precio=producto_precio, marca=producto_marca)
            producto.save()

            return redirect(reverse_lazy('productos'))
    else:

        miForm = ProductoForm()

    return render(request, "repuestosalinstante/productoForm.html", {"form": miForm} )

@login_required
def productoUpdate(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    if request.method == "POST":
        miForm = ProductoForm(request.POST)
        if miForm.is_valid():
            producto.nombre = miForm.cleaned_data.get("nombre")
            producto.marca = miForm.cleaned_data.get("marca")
            producto.precio = miForm.cleaned_data.get("precio")
            producto.save()
            return redirect(reverse_lazy('productos')) 

    else:
        miForm = ProductoForm(initial={'nombre': producto.nombre, 'marca': producto.marca, 'precio': producto.precio})

    return render(request, "repuestosalinstante/clienteForm.html", {"form": miForm} )

@login_required
def productoDelete(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    producto.delete()
    return redirect(reverse_lazy('productos'))

#_________________CATEGORIAS DE PRODUCTOS

class CategoriaList(LoginRequiredMixin, ListView):
    model = Categoria
 
class CategoriaCreate(LoginRequiredMixin, CreateView):
    model = Categoria
    fields = ['nombre', 'descripcion', 'marca']
    success_url = reverse_lazy('categorias')

class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    model =Categoria
    fields = ['nombre', 'descripcion', 'marca']
    success_url = reverse_lazy('categorias')

class CategoriaDelete(LoginRequiredMixin, DeleteView):
    model = Categoria
    success_url = reverse_lazy('categorias') 

#____________________________CLIENTES

@login_required
def clientes(request):
    contexto ={'clientes': Cliente.objects.all().order_by('nombre')} 
    return render(request, 'repuestosalinstante/clientes.html', contexto)

@login_required
def clienteCreate(request):

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
            
            contexto = {'clientes': Cliente.objects.all().order_by('nombre')}
            return render(request, "repuestosalinstante/clientes.html", contexto) 

    else:
        miForm = ClienteForm()

    return render(request, "repuestosalinstante/clienteForm.html", {"form": miForm} )

@login_required
def clienteUpdate(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente.nombre = miForm.cleaned_data.get("nombre")
            cliente.direccion = miForm.cleaned_data.get("direccion")
            cliente.telefono = miForm.cleaned_data.get("telefono")
            cliente.save()
            
            contexto = {'clientes': Cliente.objects.all().order_by('nombre')}  
            return render(request, "repuestosalinstante/clientes.html", contexto) 

    else:
        miForm = ClienteForm(initial={'nombre': cliente.nombre, 'direccion': cliente.direccion, 'telefono': cliente.telefono})

    return render(request, "repuestosalinstante/clienteForm.html", {"form": miForm} )

@login_required
def clienteDelete(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    cliente.delete()
    return redirect(reverse_lazy('clientes'))

#__________________________________MARCAS

class MarcaList(LoginRequiredMixin, ListView):
    model = Marca
 
class MarcaCreate(LoginRequiredMixin, CreateView):
    model = Marca
    fields = ['nombre', 'pais_origen']
    success_url = reverse_lazy('marcas')

class MarcaUpdate(LoginRequiredMixin, UpdateView):
    model =Marca
    fields = ['nombre', 'pais_origen',]
    success_url = reverse_lazy('marcas')

class MarcaDelete(LoginRequiredMixin, DeleteView):
    model = Marca
    success_url = reverse_lazy('marcas') 

#________________________ Buscar

@login_required
def buscarProductos(request):
    return render(request, "repuestosalinstante/buscar.html")

@login_required
def encontrarProductos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        productos = Producto.objects.filter(nombre__icontains=patron)
        contexto = {"productos": productos}
        return render(request, "repuestosalinstante/productos.html", contexto)
    

    contexto = {'productos': Producto.objects.all()}
    return render(request, "repuestosalinstante/productos.html", contexto) 

#______________LOGIN, LOGOUT, AUTH, REGIST

def login_request(request):         
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            #________________
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar

            #________________________________________________________
            return render(request, "repuestosalinstante/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()

    return render(request, "repuestosalinstante/login.html", {"form": miForm} )

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)

        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()

    return render(request, "repuestosalinstante/registro.html", {"form": miForm} )    

#________________________EDICION DE PERFIL

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = UserEditForm(instance=usuario)

    return render(request, "repuestosalinstante/editarPerfil.html", {"form": miForm} )    
   
class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "repuestosalinstante/cambiar_clave.html"
    success_url = reverse_lazy("home")

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            #BORRAR AVATARES
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #____________________________________________________
            avatar = Avatar(user=usuario,
                            imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy('home'))
    else:
       miForm = AvatarForm()

    return render(request, "repuestosalinstante/agregarAvatar.html", {"form": miForm} )      

