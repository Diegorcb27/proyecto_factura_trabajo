from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Cliente, Contacto
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required 
from facturas.models import Factura
from .forms import ClienteForm, ContactoForm

# Create your views here.

@method_decorator(login_required, name='dispatch') 
class ClienteCreateView(CreateView):
    model = Cliente
    # fields = ["nombre", "rif", "telefono_1", "telefono_2", "email", "num_empleados"]
    form_class=ClienteForm
    
    def get_success_url(self):
      
        return reverse_lazy('cliente:cliente_list')


@method_decorator(login_required, name='dispatch') 
class ClienteListView(ListView):
    model=Cliente
    context_object_name = 'cliente_list'
    template_name = 'cliente_list.html'
    
@method_decorator(login_required, name='dispatch') 
class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ["nombre", "email"]
    template_name_suffix = "_update_form"
    
    def get_success_url(self):
      
        return reverse_lazy('cliente:cliente_list')
    
    
@method_decorator(login_required, name='dispatch') 
class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('facturas:facturas_list')
    
# CRUD CONTACTO
@method_decorator(login_required, name='dispatch') 
class ContactoCreateView(CreateView):
    model = Contacto
    form_class=ContactoForm
    
    def get_success_url(self):
      
        return reverse_lazy('cliente:cliente_list')
    
    def form_valid(self, form):
        cliente_id = self.kwargs.get('cliente_id')
        cliente = get_object_or_404(Cliente, pk=cliente_id)
        form.instance.cliente = cliente  # Establece el cliente
        return super().form_valid(form)
    


# @method_decorator(login_required, name='dispatch') 
# class ContactoListView(ListView):
#     model=Contacto
#     context_object_name = 'contacto_list'
#     template_name = 'contacto_list.html'
    
@method_decorator(login_required, name='dispatch') 
class ContactoUpdateView(UpdateView):
    model = Contacto
    fields = ["name", "cargo", "telephone", "cellphone", "extension", "email"]
    template_name_suffix = "_update_form"
    
    def get_success_url(self):
      
        return reverse_lazy('cliente:cliente_list')
    
    
@method_decorator(login_required, name='dispatch') 
class ContactoDeleteView(DeleteView):
    model = Contacto
    success_url = reverse_lazy('cliente:cliente_list')
    
    
#crearemos una funcion para mostrar las facturas del cliente
# @method_decorator(login_required, name='dispatch') 

@login_required
def facturas_por_cliente(request, cliente_id):
   cliente = get_object_or_404(Cliente, id=cliente_id)
   facturas = Factura.objects.filter(cliente=cliente)
   return render(request, 'facturas_por_cliente.html', {'cliente': cliente, 'facturas': facturas})

@login_required
def contacto_por_cliente(request, cliente_id):
   cliente = get_object_or_404(Cliente, id=cliente_id)
   contactos = Contacto.objects.filter(cliente=cliente)
   return render(request, 'cliente/contacto_por_cliente.html', {'cliente': cliente, 'contactos': contactos})


from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from facturas.models import Factura
from django.views.generic.list import ListView

def generate_pdf(request, cliente_id,  pk):

        factura = Factura.objects.get(pk=pk)
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
