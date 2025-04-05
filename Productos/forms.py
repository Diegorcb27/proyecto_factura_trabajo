from django import forms
from .models import Productos

class ProductoForm(forms.ModelForm):
    
      class Meta: 
          model = Productos
          fields = ['company_id', 'name', 'price', 'vat_rate', 'default_qty', 'currency_id', 'is_tax_exempt', 'note']  
          widgets = {
            "company_id": forms.TextInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.TextInput(attrs={"class": "form-control"}),
            "vat_rate": forms.TextInput(attrs={"class": "form-control"}),
            "default_qty": forms.TextInput(attrs={"class": "form-control"}),
            "currency_id": forms.TextInput(attrs={"class": "form-control"}),
            "is_tax_exempt": forms.TextInput(attrs={"class": "form-control"}),
            "note": forms.TextInput(attrs={"class": "form-control"}),

              
          }
    #   esto es para cambiar como se veran la labels en el proyecto
      
          labels = {
    'company_id': 'Compañia',
    'name': 'Nombre',
    'price': 'Precio',
    'vat_rate': 'Porcentaje d I.V.A',
    'default_qty': 'Cantidad',
    'currency_id': 'Tipo de moneda',
    'is_tax_exempt': 'Excento de I.V.A',
    'note': 'Nota',
    
  
}