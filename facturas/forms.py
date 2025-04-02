from django import forms
from .models import krp_invoices
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin

class krp_invoices_Form(forms.ModelForm):
    
    class Meta: 
        model = krp_invoices
        fields = ['partner_id', 'invoice_n', 'invoice_c', 'discount', 'currency_id', 'pub_note', 'pri_note']  
        widgets = {
            # 'cliente': AutocompleteSelect(
            #   Factura._meta.get_field('cliente').remote_field,
            #   admin.site, 
            #   attrs={'placeholder': 'seleccionar...'},
                
            # ),
            'invoice_n': forms.TextInput(attrs={'class':'form-control'}),
            'invoice_c': forms.TextInput(attrs={'class':'form-control'}),
            'discount': forms.NumberInput(attrs={'class':'form-control',  'placeholder':'descuento'}),
            # 'numero_factura': forms.NumberInput(attrs={'class':'form-control',  'placeholder':'Numero de control'}),
            'currency_id': forms.TextInput(attrs={'class':'form-control',  'placeholder':'tipo de moneda'}),
            'pub_note': forms.Textarea(attrs={'class':'form-control',  'placeholder':'Nota pública'}),
            'pri_note': forms.Textarea(attrs={'class':'form-control',  'placeholder':'Nota privada'}),
           
           
            
            
        }
        labels = {
        'partner_id': 'Cliente',
        'invoice_n': 'Numero de factura',
        'invoice_c': 'Número de control',
        'discount': 'Descuento',
        # 'numero_factura': 'Número de Control',
        'currency_id': 'Identificador de moneda',
        'pub_note': 'Nota pública',
        'pri_note': 'Nota privada',
        
    
        }