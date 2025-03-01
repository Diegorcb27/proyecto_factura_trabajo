from django import forms
from .models import Factura
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin

class FacturaForm(forms.ModelForm):
    
    class Meta: 
        model = Factura
        fields = ['cliente', 'rif', 'domicilio_fiscal', 'telefono', 'descripcion', 'forma_pago', 'importe', 'iva']  
        widgets = {
            # 'cliente': AutocompleteSelect(
            #   Factura._meta.get_field('cliente').remote_field,
            #   admin.site, 
            #   attrs={'placeholder': 'seleccionar...'},
                
            # ),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'importe': forms.NumberInput(attrs={'class':'form-control',  'placeholder':'importe'}),
            # 'numero_factura': forms.NumberInput(attrs={'class':'form-control',  'placeholder':'Numero de control'}),
            'rif': forms.TextInput(attrs={'class':'form-control',  'placeholder':'rif'}),
            'domicilio_fiscal': forms.Textarea(attrs={'class':'form-control',  'placeholder':'Domicilio'}),
            'telefono': forms.NumberInput(attrs={'class':'form-control',  'placeholder':'telefono'}),
            'forma_pago': forms.Textarea(attrs={'class':'form-control',  'placeholder':'forma de pago'}),
            'iva': forms.Select(attrs={'class':'form-control',  'placeholder':'I.V.A'}),
           
            
            
        }
    labels = {
    'cliente': 'Cliente',
    'descripcion': 'Descripción',
    'importe': 'Importe',
    'iva': 'IVA',
    # 'numero_factura': 'Número de Control',
    'rif': 'R.I.F',
    'domicilio_fiscal': 'Domicilio Fiscal',
    'telefono': 'Teléfono',
    'forma_pago': 'Forma de Pago',
  
}