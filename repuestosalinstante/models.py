from django.db import models


# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    marca = models.CharField(max_length=50)

    class Meta:
        ordering = ["-nombre"]

    def __str__(self):
        return f"{self.nombre}"

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    país_origen = models.CharField(max_length=50)
    año_lanzamiento = models.IntegerField(verbose_name="Año de lanzamiento")


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='categorias', null=True, blank=True)

