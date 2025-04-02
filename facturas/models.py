from django.db import models
# from django.contrib.auth.models import User
from Cliente.models import krp_partners


# Create your models here.




class krp_invoices(models.Model):
    # usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    partner_id = models.ForeignKey(krp_partners, on_delete=models.CASCADE)
    invoice_n = models.CharField(max_length=20, unique=True)
    invoice_d = models.DateTimeField(auto_now_add=True)
    invoice_c = models.CharField(max_length=7)  # Código de factura
    discount = models.DecimalField(max_digits=15, decimal_places=2, default=0)  # Descuento predeterminado como 0
    currency_id = models.CharField(max_length=4, blank=True, null=True)  # Identificador de moneda (opcional)
    pub_note = models.CharField(max_length=255, blank=True, null=True)  # Nota pública (opcional)
    pri_note = models.CharField(max_length=255, blank=True, null=True)  # Nota privada (opcional)

    
    
class  krp_invoice_transactions(models.Model):
    invoice_id = models.ForeignKey(krp_invoices, on_delete=models.CASCADE)  # Relación con una factura (idealmente ForeignKey en un modelo más complejo)
    product_id = models.BigIntegerField()  # Relación con un producto
    price = models.DecimalField(max_digits=15, decimal_places=2)  # Precio con precisión decimal
    qty = models.PositiveIntegerField()  # Cantidad numérica positiva
    amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)  # Puede ser opcional
    vat_rate = models.DecimalField(max_digits=5, decimal_places=2)  # Tasa de IVA
    currency_id = models.CharField(max_length=4)  # Identificador de moneda
    curr_rate = models.DecimalField(max_digits=9, decimal_places=5, default=0)  # Tasa de cambio con valor por defecto
    note = models.CharField(max_length=255, blank=True, null=True)  # Nota opcional

    def calcular_total(self):
        """
        Calcula el total basado en el precio, cantidad y tasa de IVA.
        """
        total_sin_iva = self.price * self.qty
        total_con_iva = total_sin_iva + (total_sin_iva * self.vat_rate / 100)
        return total_con_iva

    def __str__(self):
        """
        Devuelve una representación en cadena de la transacción.
        """
        return f'Transacción de Factura ID {self.invoice_id}'
