from django.db import models
from django.shortcuts import get_object_or_404

# Create your models here.

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
    


    
    

