from django.db import models
from django.shortcuts import get_object_or_404

# Create your models here.

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    rif= models.CharField(max_length=12, unique=True, default='J-')
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono_1= models.CharField(max_length=15, default='default_value')
    telefono_2 = models.CharField(max_length=15, default='default_value')
    fecha_contrato=models.DateField(auto_now=True)
    num_empleados = models.IntegerField(default=0)
    
    

    def __str__(self):
        return self.nombre
    
class Contacto(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='contactos')
    cargo = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15, default='default_value')
    cellphone = models.CharField(max_length=15, default='default_value')
    extension = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField()
    
    def __str__(self):
        return f" {self.name} con ID: ({self.id})"
    


    
    

