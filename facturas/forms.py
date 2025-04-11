from django import forms
from .models import Facturas, Productos, Clientes, ClienteDireccion, ClienteContactos
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin

class Facturas_Form(forms.ModelForm):
    
    class Meta: 
        model = Facturas
        fields = ['partner_id', 'invoice_n', 'invoice_d', 'invoice_c', 'discount', 'currency_id', 'pub_note', 'pri_note']  
        widgets = {
            # 'cliente': AutocompleteSelect(
            #   Factura._meta.get_field('cliente').remote_field,
            #   admin.site, 
            #   attrs={'placeholder': 'seleccionar...'},
                
            # ),
            'invoice_d': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
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
        'invoice_d': 'Fecha',
        'invoice_n': 'Numero de factura',
        'invoice_c': 'Número de control',
        'discount': 'Descuento',
        # 'numero_factura': 'Número de Control',
        'currency_id': 'Identificador de moneda',
        'pub_note': 'Nota pública',
        'pri_note': 'Nota privada',
        
    
        }
        
#Formulario de Productos

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
    'vat_rate': 'Porcentaje de I.V.A',
    'default_qty': 'Cantidad',
    'currency_id': 'Tipo de moneda',
    'is_tax_exempt': 'Excento de I.V.A',
    'note': 'Nota',
    
  
}
          
#Formulario de productos
class ClienteForm(forms.ModelForm):
    
      class Meta: 
          model = Clientes
          fields = ['tin', 'name', 'email', 'partner_type', 'is_tax_exempt', 'economy_sector', 'website', 'phone1', 'phone2', 'empl_size', 'pub_note', 'pri_note']  
          widgets = {
            "tin": forms.TextInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "partner_type": forms.TextInput(attrs={"class": "form-control"}),
            "is_tax_exempt": forms.TextInput(attrs={"class": "form-control"}),
            "economy_sector": forms.TextInput(attrs={"class": "form-control"}),
            "website": forms.TextInput(attrs={"class": "form-control"}),
            "phone1": forms.TextInput(attrs={"class": "form-control"}),
            "phone2": forms.TextInput(attrs={"class": "form-control"}),
            "pub_note": forms.Textarea(attrs={"class": "form-control"}),
            "pri_note": forms.Textarea(attrs={"class": "form-control"}),
            "empl_size": forms.NumberInput(attrs={"class": "form-control"})
              
          }
    #   esto es para cambiar como se veran la labels en el proyecto
      
          labels = {
    'tin': 'R.I.F',
    'name': 'Nombre',
    'email': 'Email',
    'partner_type': 'Tipo de cliente',
    'is_tax_exempt': 'Exempto de impuesto',
    'economy_sector': 'Sector economico',
    'website': 'Pagina Web',
    'phone1': 'Telefono 1',
    # 'numero_factura': 'Número de Control',
    'phone2': 'Telefono 2',
    'pub_note': 'Nota pública',
    'pri_note': 'Nota privada',
    'empl_size': 'Numero de empleados',
  
}
          
class ClienteDireccionForm(forms.ModelForm):
    
      class Meta: 
          model =  ClienteDireccion
          fields = ['address_type', 'address_lines', 'ref_address', 'state_id', 'city', 'municipality', 'parish', 'postal_code']  
          widgets = {
            "address_type": forms.TextInput(attrs={"class": "form-control"}),
            "address_lines": forms.TextInput(attrs={"class": "form-control"}),
            "ref_address": forms.TextInput(attrs={"class": "form-control"}),
            "country_id": forms.TextInput(attrs={"class": "form-control"}),
            "state_id": forms.TextInput(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "municipality": forms.TextInput(attrs={"class": "form-control"}),
            "parish": forms.TextInput(attrs={"class": "form-control"}),
            "postal_code": forms.TextInput(attrs={"class": "form-control"}),
            
              
          }
    #   esto es para cambiar como se veran la labels en el proyecto
      
          labels = {
    'address_type': 'Tipo de dirección',
    'address_lines': 'Dirección',
    'ref_address': 'Dirección de referencia',
    'country_id': 'País',
    'state_id': 'Estado',
    'city': 'Ciudad',
    'municipality': 'Municipio',
    'parish': 'Parroquia',
    'postal_code': 'Código Postal',
   
  
}
          
          
class ContactoForm(forms.ModelForm):
    
      class Meta: 
          model = ClienteContactos
          fields = ['partner_id', 'firstname', 'middlename', 'lastname1', 'lastname2', 'position', 'phone', 'phone_ext', 'mobile', 'email', 'in_invoice']  
          widgets = {
            "firstname": forms.TextInput(attrs={"class": "form-control"}),
            "middlename": forms.TextInput(attrs={"class": "form-control"}),
            "lastname1": forms.TextInput(attrs={"class": "form-control"}),
            "lastname2": forms.TextInput(attrs={"class": "form-control"}),
            "position": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "phone_ext": forms.TextInput(attrs={"class": "form-control"}),
            "mobile": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "in_invoice": forms.TextInput(attrs={"class": "form-control"}),
            
              
          }
    #   esto es para cambiar como se veran la labels en el proyecto
      
          labels = {
    'partner_id': 'Cliente',
    'firstname': 'Primer nombre',
    'middlename': 'Segundo nombre',
    'lastname1': 'Primer apellido',
    'lastname2': 'Segundo apellido',
    'position': 'Cargo',
    'phone': 'Telefono',
    'phone_ext': 'Extension',
    'mobile': 'Celular',
    'email': 'Email',
    'in_invoice': 'Facturar',
  
}