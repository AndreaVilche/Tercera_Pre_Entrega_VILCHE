from django.db import models


# Create your models here.
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


