from django.contrib import admin
from  .models import *

# Register your models here.

admin.site.register(Producto)

admin.site.register(Vendedor)

admin.site.register(Comprador)

admin.site.register(Oferta)
