from django.contrib import admin
from .models import Factura

# Register your models here.

# @admin.register(Factura)
# class FacturaAdmin(admin.ModelAdmin):
#     list_display = ('id', 'usuario', 'fecha', 'importe')

# class FacturaAdmin(admin.ModelAdmin):
#     list_display = ['numero_factura', 'cliente', 'fecha', 'importe', 'iva']  # Actualiza 'total' a 'importe'

# admin.site.register(Factura, FacturaAdmin)

# admin.py
from django.contrib import admin
from .models import Cliente, Factura

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    autocomplete_fields = ['cliente']