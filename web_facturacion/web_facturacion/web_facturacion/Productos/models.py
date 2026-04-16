from django.db import models

# Create your models here.

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
      
    