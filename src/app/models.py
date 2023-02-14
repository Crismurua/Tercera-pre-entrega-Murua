from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    precio = models.FloatField()
    
class Vendedor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    ventas = models.IntegerField()
    
class Comprador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    compras = models.IntegerField()
    
class Oferta(models.Model):
    producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    total = models.FloatField()