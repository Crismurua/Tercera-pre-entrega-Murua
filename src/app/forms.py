from django import forms


class ProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    cantidad = forms.IntegerField()
    precio = forms.FloatField()


class VendedorFormulario(forms.Form):   
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    ventas = forms.IntegerField()
    

class CompradorFormulario(forms.Form):   
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    compras = forms.IntegerField()
    
class OfertaFormulario(forms.Form):
    producto = forms.CharField(max_length=50)
    cantidad = forms.IntegerField()
    total = forms.FloatField()