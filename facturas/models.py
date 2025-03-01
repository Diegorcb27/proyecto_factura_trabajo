from django.db import models
# from django.contrib.auth.models import User
from Cliente.models import Cliente


# Create your models here.




class Factura(models.Model):
    IVA_CHOICES = [
        (8, '8%'),
        (12, '12%'),
        (16, '16%'),
    ]

    # usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero_factura = models.CharField(max_length=20, unique=True)
    fecha = models.DateTimeField(auto_now_add=True)
    rif = models.CharField(max_length=12, unique=True, default='J-')
    domicilio_fiscal = models.TextField(default="Sin domicilio")  # Define un valor predeterminado
    telefono = models.CharField(max_length=15, default='default_value')
    descripcion = models.TextField()
    forma_pago = models.TextField()
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.IntegerField(choices=IVA_CHOICES, default=16)

    def calcular_total_con_iva(self):
        return self.importe + (self.importe * self.iva / 100)

    def save(self, *args, **kwargs):
        self.control()  # Aquí se llama al método control
        super(Factura, self).save(*args, **kwargs)

    def control(self):
        if not self.numero_factura:
            last_invoice = Factura.objects.all().order_by('id').last()
            if last_invoice:
                last_number = int(last_invoice.numero_factura)
                new_number = last_number + 1
            else:
                new_number = 1
            self.numero_factura = f"{new_number:06d}"

    def __str__(self):
        return f'Factura {self.numero_factura} - {self.cliente}'
