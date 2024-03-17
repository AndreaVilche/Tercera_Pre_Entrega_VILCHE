from django.contrib import admin
from .models import Cliente, Producto, Marca
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion')

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Marca)