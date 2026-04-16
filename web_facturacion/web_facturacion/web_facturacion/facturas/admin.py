from django.contrib import admin
from .models import Facturas

# Register your models here.

# @admin.register(Factura)
# class FacturaAdmin(admin.ModelAdmin):
#     list_display = ('id', 'usuario', 'fecha', 'importe')

# class FacturaAdmin(admin.ModelAdmin):
#     list_display = ['numero_factura', 'cliente', 'fecha', 'importe', 'iva']  # Actualiza 'total' a 'importe'

# admin.site.register(Factura, FacturaAdmin)

# admin.py
from django.contrib import admin
from .models import Facturas, Clientes

@admin.register(Clientes)
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Facturas)
class FacturaAdmin(admin.ModelAdmin):
    autocomplete_fields = ['partner_id']