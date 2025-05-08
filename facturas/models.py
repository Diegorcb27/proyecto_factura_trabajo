from django.db import models
from django.utils.timezone import now
# from django.contrib.auth.models import User



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


class Clientes(models.Model): #Clientes
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    tin= models.CharField(max_length=12, unique=True, default='J-')
    partner_type=models.CharField(max_length=24)
    is_tax_exempt = models.IntegerField(choices=((0, 'False'), (1, 'True')), default=0)
    economy_sector=models.CharField(max_length=24)
    website=models.CharField(max_length=64)
    email = models.EmailField()
    contract_d=models.DateField(auto_now=True)
    empl_size = models.IntegerField(default=0)
    phone1= models.CharField(max_length=15, default='default_value')
    phone2 = models.CharField(max_length=15, default='default_value')
    pub_note = models.CharField(max_length=255)   
    pri_note = models.CharField(max_length=255)   
    
    def __str__(self):
        return self.name
    
 #Productos
class Productos(models.Model): #Productos
    id = models.AutoField(primary_key=True)
    company_id = models.CharField(max_length=24)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2) 
    vat_rate = models.DecimalField(max_digits=5, decimal_places=2)
    default_qty = models.PositiveIntegerField() 
    currency_id = models.CharField(max_length=4)
    is_tax_exempt = models.IntegerField(choices=((0, 'False'), (1, 'True')), default=0)
    note = models.CharField(max_length=255) 
    
    def __str__(self):
        return self.name  
    
class Facturas(models.Model): #Facturas
    # usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    partner_id = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    invoice_n = models.CharField(max_length=20, unique=True)
    invoice_d = models.DateTimeField(default=now)
    invoice_c = models.CharField(max_length=7)  # Código de factura
    discount = models.DecimalField(max_digits=15, decimal_places=2, default=0)  # Descuento predeterminado como 0
    currency_id = models.CharField(max_length=4, blank=True, null=True)  # Identificador de moneda (opcional)
    pub_note = models.CharField(max_length=255, blank=True, null=True)  # Nota pública (opcional)
    pri_note = models.CharField(max_length=255, blank=True, null=True)  # Nota privada (opcional)
    
    def __str__(self):
        return self.invoice_n
    
    def get_factura_transaction(self):
        return self.transacciones.all()

        # return self.facturastransactions_set.all()#me trae las facturas transaction relacionadas a esta factura

    
    
class  FacturasTransactions(models.Model): #krp_invoice_transactions
    invoice_id = models.ForeignKey(Facturas, on_delete=models.CASCADE, related_name="transacciones")  # Relación con una factura (idealmente ForeignKey en un modelo más complejo)
    product_id = models.ForeignKey(Productos, on_delete=models.CASCADE)  # Relación con un producto
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
        return f'Transacción de Factura ID {self.invoice_id} y {self.product_id}'
    
   
    
    #Clientes
    

from django.db import models

class ClienteDireccion(models.Model): #krp_partner_address
    
    partner_id = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='addresses')
    address_type = models.CharField(max_length=24)  # Representa varchar(24) not null
    address_lines = models.CharField(max_length=120, blank=True, null=True)  # Representa varchar(120)
    ref_address = models.CharField(max_length=64, blank=True, null=True)  # Representa varchar(64)
    country_id = models.CharField(max_length=64, blank=True, null=True)  # Representa varchar(4)
    state_id = models.CharField(max_length=64, blank=True, null=True)  # Representa varchar(4)
    city = models.CharField(max_length=64, blank=True, null=True)  # Representa varchar(64)
    municipality = models.CharField(max_length=64, blank=True, null=True)  # Representa varchar(64)
    parish = models.CharField(max_length=64, blank=True, null=True)  # Representa varchar(64)
    postal_code = models.CharField(max_length=10, blank=True, null=True)  # Representa varchar(10)

    def __str__(self):
        return f"{self.address_type} - {self.city}, {self.state_id}"

    
class ClienteContactos(models.Model): #ClienteContactos
    id = models.AutoField(primary_key=True)
    partner_id = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='contactos')
    firstname = models.CharField(max_length=17)
    middlename = models.CharField(max_length=15)
    lastname1 = models.CharField(max_length=17)
    lastname2 = models.CharField(max_length=15)
    position = models.CharField(max_length=64)
    phone = models.CharField(max_length=15, default='default_value')
    phone_ext = models.CharField(max_length=6, blank=True, null=True)
    mobile = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField()
    in_invoice = models.IntegerField(choices=((0, 'False'), (1, 'True')), default=0)
    
    def __str__(self):
        return f" {self.firstname} con ID: ({self.id})"
