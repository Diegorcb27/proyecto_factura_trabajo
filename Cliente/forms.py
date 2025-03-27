from django import forms
from .models import Cliente, Contacto

class ClienteForm(forms.ModelForm):
    
      class Meta: 
          model = Cliente
          fields = ['rif', 'nombre', 'email', 'telefono_1', 'telefono_2', 'num_empleados']  
          widgets = {
            "rif": forms.TextInput(attrs={"class": "form-control"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "telefono_1": forms.TextInput(attrs={"class": "form-control"}),
            "telefono_2": forms.TextInput(attrs={"class": "form-control"}),
            "num_empleados": forms.NumberInput(attrs={"class": "form-control"})
              
          }
    #   esto es para cambiar como se veran la labels en el proyecto
      
          labels = {
    'rif': 'R.I.F',
    'nombre': 'Nombre',
    'email': 'Email',
    'telefono_1': 'Telefono 1',
    # 'numero_factura': 'Número de Control',
    'telefono_2': 'Telefono 2',
    'num_empleados': 'Numero de empleados',
  
}
          
          
class ContactoForm(forms.ModelForm):
    
      class Meta: 
          model = Contacto
          fields = ['name', 'cargo', 'telephone', 'cellphone', 'extension', "email"]  
          widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "cargo": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "telephone": forms.TextInput(attrs={"class": "form-control"}),
            "cellphone": forms.TextInput(attrs={"class": "form-control"}),
            "extension": forms.NumberInput(attrs={"class": "form-control"})
              
          }
    #   esto es para cambiar como se veran la labels en el proyecto
      
          labels = {
    'name': 'Nombre',
    'cargo': 'Cargo',
    'email': 'Email',
    'telephone': 'Telefono',
    'cellphone': 'Celular',
    'extension': 'Extension',
  
}