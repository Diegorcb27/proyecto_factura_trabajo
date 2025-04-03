from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from .models import krp_partners, krp_partner_contacts, krp_partner_address
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required 
from facturas.models import krp_invoices
from .forms import ClienteForm, ContactoForm
from django.http import HttpResponseRedirect


# Create your views here.

@method_decorator(login_required, name='dispatch') 
class ClienteCreateView(CreateView):
    model = krp_partners
    # fields = ["nombre", "rif", "telefono_1", "telefono_2", "email", "num_empleados"]
    form_class=ClienteForm
    
    def get_success_url(self):
      
        return reverse_lazy('cliente:cliente_list')


@method_decorator(login_required, name='dispatch') 
class ClienteListView(ListView):
    model=krp_partners
    context_object_name = 'cliente_list'
    template_name = 'cliente_list.html'
    
@method_decorator(login_required, name='dispatch') 
class ClienteUpdateView(UpdateView):
    model = krp_partners
    # fields = ["rif", "nombre", "email", "telefono_1", "telefono_2", "num_empleados"]
    form_class=ClienteForm
    template_name_suffix = "_update_form"
    
    
    def get_success_url(self):
      
        return reverse_lazy('cliente:cliente_list')
    
    
@method_decorator(login_required, name='dispatch') 
class ClienteDeleteView(DeleteView):
    model = krp_partners
    success_url = reverse_lazy('cliente:cliente_list')
    
@method_decorator(login_required, name='dispatch') 
class ClienteDetailView(DetailView):
    model = krp_partners
    context_object_name = 'partner' #con este atributo puedo usar este nombre para acceder al modelo de cada cliente en particular
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
    
#CRUD DIRECCION CLIENTE

# Crear dirección
class PartnerAddressCreateView(CreateView):
    model = krp_partner_address
    fields = ['address_type', 'address_lines', 'ref_address', 'country_id', 'state_id', 'city', 'municipality', 'parish', 'postal_code']
    template_name = 'Cliente/partner_address_form.html'
    def get_success_url(self):
        
        return reverse_lazy('cliente:cliente_list')
    
   
    


# Listar direcciones
class PartnerAddressListView(ListView):
    model = krp_partner_address
    template_name = 'Cliente/partner_address_list.html'
    context_object_name = 'addresses'

# Detalle de dirección
class PartnerAddressDetailView(DetailView):
    model = krp_partner_address
    template_name = 'Cliente/partner_address_detail.html'
    context_object_name = 'partner'
    
    def get_object(self):
        # Maneja el error 404 si el objeto no se encuentra
        return get_object_or_404(krp_partner_address, pk=self.kwargs['pk'])
    

class PartnerAddressUpdateView(UpdateView):
    model = krp_partner_address
    fields = ['address_type', 'address_lines', 'ref_address', 'country_id', 'state_id', 'city', 'municipality', 'parish', 'postal_code']
    template_name = 'Cliente/partner_address_update_form.html'
    
    def get_object(self):
        return get_object_or_404(krp_partner_address, pk=self.kwargs['pk'])
    
    def get_success_url(self):
      
        return reverse_lazy('cliente:cliente_list')


# Eliminar dirección
class PartnerAddressDeleteView(DeleteView):
    model = krp_partner_address
    template_name = 'Cliente/partner_address_confirm_delete.html'
    def get_object(self):
        # Usa el pk de la URL para buscar el objeto de dirección
        return get_object_or_404(krp_partner_address, pk=self.kwargs['pk'])

    def get_success_url(self):
        # Redirige a la vista de detalle del cliente
        return reverse('cliente:cliente_detail', kwargs={'pk': self.object.partner_id.id})
    
# CRUD CONTACTO
@method_decorator(login_required, name='dispatch') 
class ContactoCreateView(CreateView):
    model = krp_partner_contacts
    form_class=ContactoForm
    
    def get_success_url(self):
      
        return reverse_lazy('cliente:cliente_list')
    
    def form_valid(self, form):
        partner = get_object_or_404(krp_partners, pk=self.kwargs['cliente_id'])  # Obtén el objeto relacionado
        form.instance.partner_id = partner  # Asocia el `partner_id` al formulario
        return super().form_valid(form)
    


# @method_decorator(login_required, name='dispatch') 
# class ContactoListView(ListView):
#     model=Contacto
#     context_object_name = 'contacto_list'
#     template_name = 'contacto_list.html'
    
@method_decorator(login_required, name='dispatch') 
class ContactoUpdateView(UpdateView):
    model = krp_partner_contacts
    # fields = ["name", "cargo", "telephone", "cellphone", "extension", "email"]
    form_class=ContactoForm
    template_name_suffix = "_update_form"
    
    def get_success_url(self):
      
        return reverse_lazy('cliente:cliente_list')
    
    
@method_decorator(login_required, name='dispatch') 
class ContactoDeleteView(DeleteView):
    model =  krp_partner_contacts
    success_url = reverse_lazy('cliente:cliente_list')
    
    
#crearemos una funcion para mostrar las facturas del cliente
# @method_decorator(login_required, name='dispatch') 

@login_required
def facturas_por_cliente(request, cliente_id):
   cliente = get_object_or_404(krp_partners, id=cliente_id)
   facturas = krp_invoices.objects.filter(partner_id=cliente)
   return render(request, 'facturas_por_cliente.html', {'cliente': cliente, 'facturas': facturas})

#Filtro el contacto por cliente
@login_required
def contacto_por_cliente(request, cliente_id):
   cliente = get_object_or_404(krp_partners, id=cliente_id)
   contactos = krp_partner_contacts.objects.filter(partner_id=cliente)
   return render(request, 'cliente/contacto_por_cliente.html', {'cliente': cliente, 'contactos': contactos})

@login_required
def direccion_por_cliente(request, cliente_id):
    # Obtener el cliente específico
    cliente = get_object_or_404(krp_partners, id=cliente_id)
    
    # Obtener las direcciones asociadas al cliente
    direcciones = krp_partner_address.objects.filter(partner_id=cliente)
    
    # Renderizar la plantilla con los datos
    return render(request, 'cliente/direccion_por_cliente.html', {'cliente': cliente, 'direcciones': direcciones})


from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from facturas.models import krp_invoices
from django.views.generic.list import ListView

def generate_pdf(request, cliente_id,  pk):

        factura = krp_invoices.objects.get(pk=pk)
        template = get_template('facturas/factura_detail_pdf.html')
        context = {
            "cliente": factura.cliente,
            "numero_factura": factura.numero_factura,
            "rif": factura.rif,
            "domicilio": factura.domicilio_fiscal,
            "telefono": factura.telefono,
            "descripcion": factura.descripcion,
            "forma_pago": factura.forma_pago,
            "Importe": factura.importe,
            "iva":factura.iva,
            "total": factura.calcular_total_con_iva,
            "id": factura.id,
            
            
        }
        html_template = template.render(context)
        pdf_file = HTML(string=html_template).write_pdf(target=f"factura_{pk}.pdf")
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="output.pdf"'
        print(pk)
        return response
