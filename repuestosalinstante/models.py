from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE, related_name='categorias', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre}, {self.descripcion}, {self.marca}"


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    marca = models.CharField(max_length=50)
    class Meta:
        ordering = ["nombre"]    

    def __str__(self):
        return f"{self.nombre}, {self.marca}, {self.precio}"

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    pais_origen = models.CharField(max_length=50)
    class Meta:
        ordering = ["nombre"]    

    def __str__(self):
        return f"{self.nombre}, {self.pais_origen}"    


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    class Meta:
        ordering = ["nombre"]   
    def __str__(self):
        return f"{self.nombre}, {self.direccion}"

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")   
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"        


