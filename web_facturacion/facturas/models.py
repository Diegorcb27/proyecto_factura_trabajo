from django.db import models
# from django.contrib.auth.models import User
from Cliente.models import Clientes


# Create your models here.

from django.db import models

class Referencias(models.Model):
    domain_name = models.CharField(
        max_length=32, 
        help_text="Dominio o nombre de información."
    )
    item_value = models.CharField(
        max_length=24, 
        help_text="Identificador elemento o valor."
    )
    group_value = models.CharField(
        max_length=24, 
        null=True, 
        blank=True, 
        help_text="Grupo del valor asociado."
    )
    meaning = models.CharField(
        max_length=64, 
        null=True, 
        blank=True, 
        help_text="Nombre o descripción de elemento."
    )
    mean_label = models.CharField(
        max_length=64, 
        null=True, 
        blank=True, 
        help_text="Etiqueta o descripción del elemento."
    )
    order_val = models.DecimalField(
        max_digits=7, 
        decimal_places=3, 
        null=True, 
        blank=True, 
        help_text="Valor de orden numérico."
    )

    class Meta:
        db_table = "Referencias"
        verbose_name = "Referencia"
        verbose_name_plural = "Referencias"
        


class Compañia(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    instance = models.DecimalField(max_digits=10, decimal_places=0)
    name = models.CharField(max_length=64)
    shortening = models.CharField(max_length=32)
    lic_key = models.CharField(max_length=20)
    tin = models.CharField(max_length=20)
    country_id = models.CharField(max_length=4)
    nationality = models.CharField(max_length=24, null=True, blank=True)
    natural_code = models.CharField(max_length=3, null=True, blank=True)
    foreign_code = models.CharField(max_length=3, null=True, blank=True)
    email_cfg_file = models.CharField(max_length=64, null=True, blank=True)
    gen_employee_n = models.DecimalField(max_digits=1, decimal_places=0, default=0)
    len_employee_n = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    lookat_job_sal = models.DecimalField(max_digits=1, decimal_places=0, default=0)
    start_fy = models.DecimalField(max_digits=2, decimal_places=0, default=1)
    audit_user = models.CharField(max_length=64, null=True, blank=True)
    audit_dte = models.DateField(null=True, blank=True)
    audit_track = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    kinder_age = models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=True)
    kinder_minwage = models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=True)
    kinder_pct = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    kinder_payitem_id = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True)
    lookat_dep_job = models.DecimalField(max_digits=1, decimal_places=0, default=0)
    lookat_job_quota = models.CharField(max_length=24, default='na')
    filename_logo = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        db_table = "Compañia"



class Facturas(models.Model): #Facturas
    # usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    partner_id = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    invoice_n = models.CharField(max_length=20, unique=True)
    invoice_d = models.DateTimeField(auto_now_add=True)
    invoice_c = models.CharField(max_length=7)  # Código de factura
    discount = models.DecimalField(max_digits=15, decimal_places=2, default=0)  # Descuento predeterminado como 0
    currency_id = models.CharField(max_length=4, blank=True, null=True)  # Identificador de moneda (opcional)
    pub_note = models.CharField(max_length=255, blank=True, null=True)  # Nota pública (opcional)
    pri_note = models.CharField(max_length=255, blank=True, null=True)  # Nota privada (opcional)

    
    
class  FacturasTransactions(models.Model): #krp_invoice_transactions
    invoice_id = models.ForeignKey(Facturas, on_delete=models.CASCADE)  # Relación con una factura (idealmente ForeignKey en un modelo más complejo)
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
