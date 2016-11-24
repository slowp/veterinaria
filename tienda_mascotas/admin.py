from django.contrib import admin
from tienda_mascotas.models import Animal,Cliente,Adopcion

# Register your models here.
admin.site.register(Animal)
admin.site.register(Cliente)
admin.site.register(Adopcion)