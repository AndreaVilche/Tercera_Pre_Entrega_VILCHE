from django import forms

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    precio = forms.IntegerField(required=True)
    marca = forms.CharField(max_length=50, required=True)

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=60, required=True)
    direccion = forms.CharField(max_length=60, required=True)
    telefono = forms.IntegerField(required=True)

class MarcaForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    pais_origen = forms.CharField(max_length=50, required=True)
