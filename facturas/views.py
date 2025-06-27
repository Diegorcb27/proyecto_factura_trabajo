from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import Facturas, FacturasTransactions, Productos, Clientes, ClienteContactos, ClienteDireccion
from .forms import Facturas_Form, ProductoForm, ClienteDireccionForm, ClienteForm, ContactoForm, FacturasTransactionsForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from django.shortcuts import redirect, get_object_or_404, render
from django.utils import timezone
from django.forms import modelformset_factory
from django.contrib import messages
from django.db import transaction  # Importación faltante


#estas dos importaciones es para saber si el usuario es miembro del staff y evitarnos la condicion del mixin
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required #IMPORTANTE: me permite saber si el usuario se registro

# Create your views here.


class StaffRequiredMixin(object): #Este mixin requerira que el usuario sea miembro del staff
    @method_decorator(staff_member_required) #este decorador es para verificar si el usuario es staff o no
    def dispatch(self, request, *args, **kwargs):
        print(request.user)
        # if not request.user.is_staff: #esto es para saber si el usuario ha iniciado sesion en el admin, si no ha iniciado te redirecciona al admin
        #     return redirect(reverse_lazy("admin:login"))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs) #el dispatch procesa la peticiones al servidor
    

@method_decorator(login_required, name='dispatch') #este decorador es para verificar si el usuario es staff y asi poder usar estas funcionalidades
class FacturaCreateView(CreateView):
    model = Facturas
    form_class = Facturas_Form
    # template_name = 'facturas/factura_form.html'  # Asegúrate de que esta plantilla exista
    
            
    def get_success_url(self):
        return reverse_lazy('facturas:facturas_list')
  
 

    def form_invalid(self, form):
        """
        Renderiza la vista con los errores del formulario.
        """
        context = self.get_context_data()
        messages.error(self.request, "Hubo un error al crear la factura. Por favor, revisa los datos.")
        return self.render_to_response(context)
    
  


    
@method_decorator(login_required, name='dispatch')
class FacturaListView(ListView):
    model=Facturas
    context_object_name = 'factura_list'
    template_name = 'factura_list.html'
    paginate_by=5
    
    def get_queryset(self): #ordena la factura por numero de factura
        return Facturas.objects.all().order_by('-invoice_n')
  
           
    
    
@method_decorator(login_required, name='dispatch')
class FacturaUpdateView(UpdateView):
    model = Facturas
    form_class=Facturas_Form
    # fields = ["descripcion", "total"]
    template_name_suffix = "_update_form"
    
    def get_success_url(self):
      
        return reverse_lazy('facturas:facturas_list')
    
@method_decorator(login_required, name='dispatch')

class FacturaDeleteView(DeleteView):
    model = Facturas
    success_url = reverse_lazy('facturas:facturas_list')
    

class FacturaDetailView(DetailView):
    model = Facturas
    context_object_name = 'Facturas'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        factura = self.object  # Obtiene la factura actual
        total_balance = sum(transaction.calcular_total() for transaction in FacturasTransactions.objects.filter(invoice_id=factura))
        context['total_balance'] = total_balance
        return context
    

#Vistas de transacciones

@method_decorator(login_required, name='dispatch')
class  FacturasTransactionsCreateView(CreateView):
    model = FacturasTransactions
    form_class = FacturasTransactionsForm
    template_name = 'facturas/facturas_transaction_form.html'
    
    
    def get_success_url(self):
        return reverse_lazy('facturas:facturas_list')
    
    def form_valid(self, form):
        factura = get_object_or_404(Facturas, pk=self.kwargs['product_id'])  # Obtén el objeto relacionado
        form.instance.invoice_id = factura  # Asocia el `partner_id` al formulario
        return super().form_valid(form)
    
    
    

@method_decorator(login_required, name="dispatch")
class FacturasTransactionsUpdateView(UpdateView):
     model = FacturasTransactions
     form_class = FacturasTransactionsForm
     template_name_suffix = "_update_form"
     template_name = 'facturas/facturas_transaction_update_form.html'
     
    #  def get_success_url(self):
    #     return reverse_lazy('facturas:facturas_list')
    
     def get_success_url(self):
        factura_id = self.object.invoice_id.id  # Obtener el ID de la factura asociada
        return reverse('facturas:facturas_detail', kwargs={'pk': factura_id})
    
@method_decorator(login_required, name="dispatch")

class FacturasTransactionDeleteView(DeleteView):
    model = FacturasTransactions
    template_name = 'facturas/facturas_transaction_confirm_delete.html'
    # success_url = reverse_lazy('facturas:facturas_list')
    def get_success_url(self):
        factura_id = self.object.invoice_id.id  # Obtener el ID de la factura asociada
        return reverse('facturas:facturas_detail', kwargs={'pk': factura_id})
    
    
    
    
#Vistas de Productos

#CRUD productos

@method_decorator(login_required, name='dispatch')
class ProductoCreateView(CreateView):
    model = Productos
    form_class = ProductoForm
    
    def get_success_url(self):
        return reverse_lazy('productos:productos_list')
    

@method_decorator(login_required, name='dispatch')
class ProductoListView(ListView):
    model = Productos
    paginate_by = 100  # if pagination is desired
    context_object_name = 'producto_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
    
    
@method_decorator(login_required, name='dispatch')
class ProductoUpdateView(UpdateView):
    model = Productos
    form_class = ProductoForm
    template_name_suffix = "_update_form"
    
    def get_success_url(self):
        return reverse_lazy('productos:productos_list')

@method_decorator(login_required, name='dispatch')

class ProductoDeleteView(DeleteView):
    model = Productos
    success_url = reverse_lazy('productos:productos_list')
    

@method_decorator(login_required, name='dispatch')
class ProductoDetailView(DetailView):
    model = Productos
    context_object_name="Productos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


#Vistas de Clientes
@method_decorator(login_required, name='dispatch') 
class ClienteCreateView(CreateView):
    model = Clientes
    # fields = ["nombre", "rif", "telefono_1", "telefono_2", "email", "num_empleados"]
    form_class=ClienteForm
    template_name = 'facturas/Clientes_form.html'
    
    def get_success_url(self):
      
        return reverse_lazy('cliente:cliente_list')


@method_decorator(login_required, name='dispatch') 
class ClienteListView(ListView):
    model=Clientes
    context_object_name = 'cliente_list'
    template_name = 'facturas/cliente_list.html'
    
@method_decorator(login_required, name='dispatch') 
class ClienteUpdateView(UpdateView):
    model = Clientes
    # fields = ["rif", "nombre", "email", "telefono_1", "telefono_2", "num_empleados"]
    form_class=ClienteForm
    template_name_suffix = "_update_form"
    
    
    def get_success_url(self):
      
        return reverse_lazy('cliente:cliente_list')
    
    
@method_decorator(login_required, name='dispatch') 
class ClienteDeleteView(DeleteView):
    model = Clientes
    success_url = reverse_lazy('cliente:cliente_list')
    
@method_decorator(login_required, name='dispatch') 
class ClienteDetailView(DetailView):
    model = Clientes
    context_object_name = 'partner' #con este atributo puedo usar este nombre para acceder al modelo de cada cliente en particular
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
    
#CRUD DIRECCION CLIENTE

# Crear dirección
class PartnerAddressCreateView(CreateView):
    model = ClienteDireccion
    form_class=ClienteDireccionForm
    # fields = ['address_type', 'address_lines', 'ref_address', 'country_id', 'state_id', 'city', 'municipality', 'parish', 'postal_code']
    template_name = 'facturas/cliente_direccion_form.html'
    def form_valid(self, form):
        # Obtener el cliente usando el parámetro de la URL
        cliente = get_object_or_404(Clientes, pk=self.kwargs['partner_id'])
        form.instance.partner_id = cliente  # Asigna el cliente a la dirección
        return super().form_valid(form)

    def get_success_url(self):
        # Redirige a la lista de clientes, o la página deseada
        return reverse_lazy('cliente:cliente_list')
    
   
    


# Listar direcciones
class PartnerAddressListView(ListView):
    model = ClienteDireccion
    template_name = 'facturas/cliente_direccion_list.html'
    context_object_name = 'addresses'

# Detalle de dirección
class PartnerAddressDetailView(DetailView):
    model = ClienteDireccion
    template_name = 'facturas/cliente_direccion_detail.html'
    context_object_name = 'partner'
    
    def get_object(self):
        # Maneja el error 404 si el objeto no se encuentra
        return get_object_or_404(ClienteDireccion, pk=self.kwargs['pk'])
    

class PartnerAddressUpdateView(UpdateView):
    model = ClienteDireccion
    form_class=ClienteDireccionForm
    template_name = 'facturas/cliente_direccion_update_form.html'
    
    def get_object(self):
        return get_object_or_404(ClienteDireccion, pk=self.kwargs['pk'])
    
    def get_success_url(self):
      
        return reverse_lazy('cliente:cliente_list')


# Eliminar dirección
class PartnerAddressDeleteView(DeleteView):
    model = ClienteDireccion
    template_name = 'facturas/cliente_direccion_confirm_delete.html'
    def get_object(self):
        # Usa el pk de la URL para buscar el objeto de dirección
        return get_object_or_404(ClienteDireccion, pk=self.kwargs['pk'])

    def get_success_url(self):
        # Redirige a la vista de detalle del cliente
        return reverse('cliente:cliente_detail', kwargs={'pk': self.object.partner_id.id})
    
# CRUD CONTACTO
@method_decorator(login_required, name='dispatch') 
class ContactoCreateView(CreateView):
    model = ClienteContactos
    form_class=ContactoForm
    # template_name = 'facturas/cliente_contactos_form.html'
    
    def get_success_url(self):
      
        return reverse_lazy('cliente:cliente_list')
    
    def form_valid(self, form):
        partner = get_object_or_404(Clientes, pk=self.kwargs['cliente_id'])  # Obtén el objeto relacionado
        form.instance.partner_id = partner  # Asocia el `partner_id` al formulario
        return super().form_valid(form)
    


# @method_decorator(login_required, name='dispatch') 
# class ContactoListView(ListView):
#     model=Contacto
#     context_object_name = 'contacto_list'
#     template_name = 'contacto_list.html'
    
@method_decorator(login_required, name='dispatch') 
class ContactoUpdateView(UpdateView):
    model = ClienteContactos
    # fields = ["name", "cargo", "telephone", "cellphone", "extension", "email"]
    form_class=ContactoForm
    template_name_suffix = "_update_form"
    
    def get_success_url(self):
      
        return reverse_lazy('cliente:cliente_list')
    
    
@method_decorator(login_required, name='dispatch') 
class ContactoDeleteView(DeleteView):
    model =  ClienteContactos
    success_url = reverse_lazy('cliente:cliente_list')
    
    
#crearemos una funcion para mostrar las facturas del cliente
# @method_decorator(login_required, name='dispatch') 

@login_required
def facturas_por_cliente(request, cliente_id):
   cliente = get_object_or_404(Clientes, id=cliente_id)
   facturas = Facturas.objects.filter(partner_id=cliente)
   return render(request, 'facturas/facturas_por_cliente.html', {'cliente': cliente, 'facturas': facturas})

#Filtro el contacto por cliente
@login_required
def contacto_por_cliente(request, cliente_id):
   cliente = get_object_or_404(Clientes, id=cliente_id)
   contactos = ClienteContactos.objects.filter(partner_id=cliente)
   return render(request, 'facturas/contacto_por_cliente.html', {'cliente': cliente, 'contactos': contactos})

@login_required
def direccion_por_cliente(request, cliente_id):
    # Obtener el cliente específico
    cliente = get_object_or_404(Clientes, id=cliente_id)
    
    # Obtener las direcciones asociadas al cliente
    direcciones = ClienteDireccion.objects.filter(partner_id=cliente)
    
    # Renderizar la plantilla con los datos
    return render(request, 'facturas/direccion_por_cliente.html', {'cliente': cliente, 'direcciones': direcciones})






#generar PDF

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from django.http import HttpResponse
from reportlab.lib.units import inch

# def generate_pdf(request, pk):
#     # Obtener datos de la factura
#     factura = Facturas.objects.get(pk=pk)

#     # Crear respuesta HTTP para el PDF
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename="factura_{pk}.pdf"'

#     # Crear el lienzo del PDF
#     pdf = canvas.Canvas(response, pagesize=letter)
#     pdf.setTitle(f"Factura de {factura.partner_id}")

#     # Estilos de texto
#     pdf.setFont("Helvetica-Bold", 16)
#     pdf.drawString(200, 750, f"Factura de {factura.partner_id}")

#     pdf.setFont("Helvetica", 12)
#     pdf.drawString(50, 720, f"Cliente: {factura.partner_id}")
#     pdf.drawString(50, 700, f"Número de factura: {factura.invoice_n}")
#     pdf.drawString(50, 680, f"Número de control: {factura.invoice_c}")
#     pdf.drawString(50, 660, f"Descuento: {factura.discount}%")
#     pdf.drawString(50, 640, f"Tipo de moneda: {factura.currency_id}")
#     pdf.drawString(50, 620, f"Nota pública: {factura.pub_note}")
#     pdf.drawString(50, 600, f"Fecha de la factura: {factura.invoice_d}")

#     # Datos de los productos en tabla
#     data = [["Producto", "Precio", "Cantidad", "IVA", "Total"]]
    
#     for product in factura.get_factura_transaction():
#         data.append([
#             product.product_id,
#             f"{product.price} bs",
#             product.qty,
#             f"{product.vat_rate}%",
#             f"{product.calcular_total()} bs"
#         ])

#     table = Table(data, colWidths=[150, 80, 80, 80, 80])
#     table.setStyle(TableStyle([
#         ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#         ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
#         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#         ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#         ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#         ('GRID', (0, 0), (-1, -1), 1, colors.black),
#     ]))

#     # Posicionar la tabla
#     table.wrapOn(pdf, 50, 500)
#     table.drawOn(pdf, 50, 550)

#     # Finalizar el PDF
#     pdf.showPage()
#     pdf.save()

#     return response

# MODELO FACTURA 1

def generate_pdf(request, pk):
    factura = Facturas.objects.get(pk=pk)
    
    def balance_subtotal(factura):
        subtotal = 0
        for transaction in factura.get_factura_transaction():
            subtotal += transaction.calcular_subtotal()
        return subtotal
    
    def balance_total(factura):
        total = 0
        for transaction in factura.get_factura_transaction():
            total += transaction.calcular_total()
        return total
    

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="factura_{pk}.pdf"'
    pdf = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # Encabezado
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(50, 750, "Cliente:")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 738, str(factura.partner_id))

    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(50, 720, "RIF:")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 708, str(factura.partner_id.tin))

    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(50, 690, "Domicilio Fiscal:")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 678, str(factura.partner_id.name))

    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(50, 660, "Contactos:")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 648, str(factura.partner_id.website))

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(400, 750, f"Factura N°: {factura.invoice_n}")
    pdf.drawString(400, 735, f"Control N°: {factura.invoice_c}")
    pdf.drawString(400, 720, f"Fecha: {factura.invoice_d.strftime('%d/%m/%Y')}")

    # Tabla de productos
    data = [["Producto", "Precio", "Cantidad", "IVA", "Total"]]
    for product in factura.get_factura_transaction():
       data.append([
            product.product_id,
            f"{product.price} bs",
            product.qty,
            f"{product.vat_rate}%",
            f"{product.calcular_subtotal():.2f} bs",
           
        ])

    table = Table(data, colWidths=[60, 220, 50, 80, 80])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (2, 1), (-1, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
    ]))
    table.wrapOn(pdf, 50, 500)
    table.drawOn(pdf, 50, 550)

    # Totales
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(400, 480, f"SUB-TOTAL Bs: {balance_subtotal(factura):.2f}")
    # pdf.drawString(400, 465, f"I.V.A. {factura.vat_rate}% Bs.: {factura.iva:.2f}")
    pdf.drawString(400, 450, f"TOTAL A PAGAR Bs: {balance_total(factura):.2f}")

    # Nota legal
    pdf.setFont("Helvetica-Oblique", 9)
    pdf.drawString(50, 400, "A los efectos de lo previsto en el Art. 25 de la ley de Impuesto al Valor Agregado,")
    pdf.drawString(50, 387, f"para efecto de conversión se ha utilizado la tasa de cambio del BCV, el 13 de julio de 2023,")
    pdf.drawString(50, 374, "Fuente: www.bcv.org.ve")

    pdf.showPage()
    pdf.save()

    return response

# MODELO FACTURA 2


    #generar Excel
from openpyxl import Workbook
from openpyxl.styles import Alignment,Border,Font,PatternFill,Side



class ReportePersonalizadoExcel(TemplateView):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        factura = Facturas.objects.get(id=pk)
        wb = Workbook()
        ws = wb.active
        ws.title = 'Reporte'

        # Convertir el objeto User a cadena de texto
        # user_str = str(factura.usuario)  # Asumiendo que 'usuario' es un campo en Factura
        # ws.append([user_str, factura.descripcion, factura.total])
        
        
            # empezamos a configurar la hoja de excel con el contenido
            
             #titulo
        ws["B1"].alignment = Alignment(horizontal="left", vertical="center") #modificamos la alineacion
        # ws["B1"].border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
        #                              top = Side(border_style="thin"), bottom = Side(border_style="thin")) #modificamos el borde
            
            #Relleno de la celda
        ws["B1"].fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
            
            #Aplicamos fuente
        ws["B1"].font = Font(name='Times New Roman', size=12, bold=True)
            
            #asignamos valor a la celda B1
        ws["B1"] = "REPORTE  DE FACTURAS PERZONALIZADO EN EXCEL CON DJANGO"
            
            #combinamos las celdas
        ws.merge_cells("B1:E1")
            
            #cmbiar anchura de la columna
        ws.column_dimensions["B"].width=35
        ws.column_dimensions["C"].width=35
        ws.column_dimensions["D"].width=35
        ws.column_dimensions["E"].width=35
            
            #cambiar el tamano de las filas
        ws.row_dimensions[1].height = 25
            
        #   crear la cabecera
       # Ajustar la alineación a la izquierda
        ws["B3"].alignment = Alignment(horizontal="left", vertical="center")

        # Mantener el borde
        # ws["B3"].border = Border(left=Side(border_style="thin"), right=Side(border_style="thin"),
        #                         top=Side(border_style="thin"), bottom=Side(border_style="thin"))

        # Cambiar el fondo a blanco
        ws["B3"].fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")

        # Cambiar la fuente a Times New Roman
        ws['B3'].font = Font(name='Times New Roman', size=12, bold=True)

        # Asignar el valor a la celda
        ws['B3'] = 'CLIENTE:'
           
            
        ws["B7"].alignment = Alignment(horizontal="left", vertical="center")

        # # Mantener el borde
        # ws["B7"].border = Border(left=Side(border_style="thin"), right=Side(border_style="thin"),
        #                         top=Side(border_style="thin"), bottom=Side(border_style="thin"))

        # Cambiar el fondo a blanco
        ws["B7"].fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")

        # Cambiar la fuente a Times New Roman
        ws['B7'].font = Font(name='Times New Roman', size=12, bold=True)

        # Asignar el valor a la celda
        ws['B7'] = 'NÚMERO DE FACTURA:'
        
       
            
         # Ajustar la alineación a la izquierda
        ws["B11"].alignment = Alignment(horizontal="left", vertical="center")

        # # Mantener el borde
        # ws["B11"].border = Border(left=Side(border_style="thin"), right=Side(border_style="thin"),
        #                         top=Side(border_style="thin"), bottom=Side(border_style="thin"))

        # Cambiar el fondo a blanco
        ws["B11"].fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")

        # Cambiar la fuente a Times New Roman
        ws['B11'].font = Font(name='Times New Roman', size=12, bold=True)

        # Asignar el valor a la celda
        ws['B11'] = 'R.I.F:'
        
        
         # Ajustar la alineación a la izquierda
        ws["B15"].alignment = Alignment(horizontal="left", vertical="center")

        # # Mantener el borde
        # ws["B15"].border = Border(left=Side(border_style="thin"), right=Side(border_style="thin"),
        #                         top=Side(border_style="thin"), bottom=Side(border_style="thin"))

        # Cambiar el fondo a blanco
        ws["B15"].fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")

        # Cambiar la fuente a Times New Roman
        ws['B15'].font = Font(name='Times New Roman', size=12, bold=True)

        # Asignar el valor a la celda
        ws['B15'] = 'DOMICILIO FISCAL:'
        
       
         # Ajustar la alineación a la izquierda
        ws["B19"].alignment = Alignment(horizontal="left", vertical="center")

        # # Mantener el borde
        # ws["B19"].border = Border(left=Side(border_style="thin"), right=Side(border_style="thin"),
        #                         top=Side(border_style="thin"), bottom=Side(border_style="thin"))

        # Cambiar el fondo a blanco
        ws["B19"].fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")

        # Cambiar la fuente a Times New Roman
        ws['B19'].font = Font(name='Times New Roman', size=12, bold=True)

        # Asignar el valor a la celda
        ws['B19'] = 'TELEFONO:'
        
         # Ajustar la alineación a la izquierda
        ws["B23"].alignment = Alignment(horizontal="left", vertical="center")

        # # Mantener el borde
        # ws["B23"].border = Border(left=Side(border_style="thin"), right=Side(border_style="thin"),
        #                         top=Side(border_style="thin"), bottom=Side(border_style="thin"))

        # Cambiar el fondo a blanco
        ws["B23"].fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")

        # Cambiar la fuente a Times New Roman
        ws['B23'].font = Font(name='Times New Roman', size=12, bold=True)

        # Asignar el valor a la celda
        ws['B23'] = 'DESCRIPCIÓN:'
       
         # Ajustar la alineación a la izquierda
        ws["B27"].alignment = Alignment(horizontal="left", vertical="center")

        # # Mantener el borde
        # ws["B27"].border = Border(left=Side(border_style="thin"), right=Side(border_style="thin"),
        #                         top=Side(border_style="thin"), bottom=Side(border_style="thin"))

        # Cambiar el fondo a blanco
        ws["B27"].fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")

        # Cambiar la fuente a Times New Roman
        ws['B27'].font = Font(name='Times New Roman', size=12, bold=True)

        # Asignar el valor a la celda
        ws['B27'] = 'FORMA DE PAGO:'
        
         # Ajustar la alineación a la izquierda
        ws["B31"].alignment = Alignment(horizontal="left", vertical="center")

        # # Mantener el borde
        # ws["B31"].border = Border(left=Side(border_style="thin"), right=Side(border_style="thin"),
        #                         top=Side(border_style="thin"), bottom=Side(border_style="thin"))

        # Cambiar el fondo a blanco
        ws["B31"].fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")

        # Cambiar la fuente a Times New Roman
        ws['B31'].font = Font(name='Times New Roman', size=12, bold=True)

        # Asignar el valor a la celda
        ws['B31'] = 'BASE IMPONIBLE:'
        
         # Ajustar la alineación a la izquierda
        ws["B35"].alignment = Alignment(horizontal="left", vertical="center")

        # Mantener el borde
        # ws["B35"].border = Border(left=Side(border_style="thin"), right=Side(border_style="thin"),
        #                         top=Side(border_style="thin"), bottom=Side(border_style="thin"))

        # Cambiar el fondo a blanco
        ws["B35"].fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")

        # Cambiar la fuente a Times New Roman
        ws['B35'].font = Font(name='Times New Roman', size=12, bold=True)

        # Asignar el valor a la celda
        ws['B35'] = 'I.V.A (%) Bs:'
    
        
          # Ajustar la alineación a la izquierda
        ws["B39"].alignment = Alignment(horizontal="left", vertical="center")

        # Mantener el borde
        # ws["B39"].border = Border(left=Side(border_style="thin"), right=Side(border_style="thin"),
        #                         top=Side(border_style="thin"), bottom=Side(border_style="thin"))

        # Cambiar el fondo a blanco
        ws["B39"].fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")

        # Cambiar la fuente a Times New Roman
        ws['B39'].font = Font(name='Times New Roman', size=12, bold=True)

        # Asignar el valor a la celda
        ws['B39'] = 'TOTAL:'
        
        
      
        
        # # Combinar las celdas de las columnas C y D
         # Definir el rango de filas que deseas combinar
        start_row = 1
        end_row = 40

        for row in range(start_row, end_row + 1):
            ws.merge_cells(start_row=row, start_column=3, end_row=row, end_column=4)
            
          #pintamos los datos
            
            
        ws.cell(row = 3, column = 3).alignment = Alignment(horizontal="left", vertical="center") #cell son celdas
        # ws.cell(row = 3, column = 3).border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
        #                             top = Side(border_style = "thin"), bottom = Side(border_style = "thin") )
        ws.cell(row = 3, column = 3).font = Font(name='Times New Roman', size=12)
        ws.cell(row = 3 , column = 3).value = str(factura.cliente)
            
        ws.cell(row = 7, column = 3).alignment = Alignment(horizontal="left", vertical="center") #cell son celdas
        # ws.cell(row = 7, column = 3).border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
        #                             top = Side(border_style = "thin"), bottom = Side(border_style = "thin") )
        ws.cell(row = 7, column = 3).font = Font(name='Times New Roman', size=12)
        factura.save()
        ws.cell(row = 7, column = 3).value = factura.numero_factura
        ws.merge_cells("C3:D3")
            
        ws.cell(row = 11, column = 3).alignment = Alignment(horizontal="left", vertical="center") #cell son celdas
        # ws.cell(row =11, column = 3).border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
        #                             top = Side(border_style = "thin"), bottom = Side(border_style = "thin") )
        ws.cell(row = 11, column = 3).font = Font(name='Times New Roman', size=12)
        ws.cell(row = 11, column = 3).value = factura.rif
        
        
        ws.cell(row = 15, column = 3).alignment = Alignment(horizontal="left", vertical="center") #cell son celdas
        # ws.cell(row =15, column = 3).border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
        #                             top = Side(border_style = "thin"), bottom = Side(border_style = "thin") )
        ws.cell(row = 15, column = 3).font = Font(name='Times New Roman', size=12)
        ws.cell(row = 15, column = 3).value = factura.domicilio_fiscal
        
        
        
        ws.cell(row = 19, column = 3).alignment = Alignment(horizontal="left", vertical="center") #cell son celdas
        # ws.cell(row =19, column = 3).border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
        #                             top = Side(border_style = "thin"), bottom = Side(border_style = "thin") )
        ws.cell(row = 19, column = 3).font = Font(name='Times New Roman', size=12)
        ws.cell(row = 19, column = 3).value = factura.telefono
        
        
        
        ws.cell(row = 23, column = 3).alignment = Alignment(horizontal="left", vertical="center") #cell son celdas
        # ws.cell(row =23, column = 3).border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
        #                             top = Side(border_style = "thin"), bottom = Side(border_style = "thin") )
        ws.cell(row = 23, column = 3).font = Font(name='Times New Roman', size=12)
        ws.cell(row = 23, column = 3).value = factura.descripcion
        
        
        ws.cell(row = 27, column = 3).alignment = Alignment(horizontal="left", vertical="center") #cell son celdas
        # ws.cell(row =27, column = 3).border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
        #                             top = Side(border_style = "thin"), bottom = Side(border_style = "thin") )
        ws.cell(row = 27, column = 3).font = Font(name='Times New Roman', size=12)
        ws.cell(row = 27, column = 3).value = factura.forma_pago
        
        
        
        ws.cell(row = 31, column = 3).alignment = Alignment(horizontal="left", vertical="center") #cell son celdas
        # ws.cell(row =31, column = 3).border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
        #                             top = Side(border_style = "thin"), bottom = Side(border_style = "thin") )
        ws.cell(row = 31, column = 3).font = Font(name='Times New Roman', size=12)
        ws.cell(row = 31, column = 3).value = str(factura.importe) + "Bs"
        
        
        
        ws.cell(row = 35, column = 3).alignment = Alignment(horizontal="left", vertical="center") #cell son celdas
        # ws.cell(row =35, column = 3).border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
        #                             top = Side(border_style = "thin"), bottom = Side(border_style = "thin") )
        ws.cell(row = 35, column = 3).font = Font(name='Times New Roman', size=12)
        ws.cell(row = 35, column = 3).value = str(factura.iva) + "%"
        
        
        
        ws.cell(row = 39, column = 3).alignment = Alignment(horizontal="left", vertical="center") #cell son celdas
        # ws.cell(row =39, column = 3).border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
        #                             top = Side(border_style = "thin"), bottom = Side(border_style = "thin") )
        ws.cell(row = 39, column = 3).font = Font(name='Times New Roman', size=12)
        ws.cell(row = 39, column = 3).value = str(factura.calcular_total_con_iva()) + "Bs"
        
        


        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="reporte_facturas.xlsx"'
        wb.save(response)
        return response

        
        
        
        
        
        
        
        
        
        # campo = int(request.GET.get('campo')) #recibe la respuesta del form y lo convierte a int
#         pk = self.kwargs.get('pk')
#         factura = Factura.objects.filter(id = pk) #solo traes los que coincidan con la edad
#         # query = Factura.objects.all()
#          # Convertir el objeto User a cadena de texto
#         user_str = str(factura.usuario)  # Asumiendo que 'usuario' es un campo en Factura
#         ws.append([user_str, factura.descripcion, factura.total])
#         wb = Workbook()
#         bandera = True #hay que hacer una validacion para que no deje la hoja en blanco cuando creemos mas hojas
#         cont = 1
#         controlador = 4 #es la posicion inicial para pintar datos
#         # for q in query: #esto es para cargar cada query en cada hoja 
#         if bandera:
#                 ws = wb.active #te permite acceder a la hoja de trabajo activa
#                 ws.title = 'Hoja'+str(cont) #le damos el nombre a la primera hoja activa
#                 bandera = False
#             # else:
#             #     ws = wb.create_sheet('Hoja'+str(cont)) #creamos otra hoja de trabajo siguiente
           
            
            
#             #empezamos a configurar la hoja de excel con el contenido
            
#              #titulo
#         ws["B1"].alignment = Alignment(horizontal="center", vertical = "center") #modificamos la alineacion
#         ws["B1"].border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
#                                      top = Side(border_style="thin"), bottom = Side(border_style="thin")) #modificamos el borde
            
#             #Relleno de la celda
#         ws["B1"].fill = PatternFill(start_color="66FFCC", end_color = "66FFCC", fill_type = "solid")
            
#             #Aplicamos fuente
#         ws["B1"].font = Font(name = "Calibri", size = 12, bold = True)
            
#             #asignamos valor a la celda B1
#         ws["B1"] = "REPORTE  DE FACTURAS PERZONALIZADO EN EXCEL CON DJANGO"
            
#             #combinamos las celdas
#         ws.merge_cells("B1:E1")
            
#             #cmbiar anchura de la columna
#         ws.column_dimensions["B"].width=20
#         ws.column_dimensions["C"].width=20
#         ws.column_dimensions["D"].width=20
#         ws.column_dimensions["E"].width=20
            
#             #cambiar el tamano de las filas
            
#         ws.row_dimensions[1].height = 25
            
#             #crear la cabecera
#         ws["B3"].alignment = Alignment(horizontal="center", vertical = "center")
#         ws["B3"].border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
#                                      top = Side(border_style="thin"), bottom = Side(border_style="thin"))
#         ws["B3"].fill = PatternFill(start_color="66CFCC", end_color = "66CFCC", fill_type = "solid")
#         ws['B3'].font = Font(name = 'Calibro', size = 10, bold = True)
#         ws['B3'] = 'Usuario'
           
            
#         ws["C3"].alignment = Alignment(horizontal="center", vertical = "center")
#         ws["C3"].border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
#                                      top = Side(border_style="thin"), bottom = Side(border_style="thin"))
#         ws["C3"].fill = PatternFill(start_color="66CFCC", end_color = "66CFCC", fill_type = "solid")
#         ws['C3'].font = Font(name = 'Calibro', size = 10, bold = True)
#         ws['C3'] = 'Descripcion'
#         ws.merge_cells("C3:D3")
            
            
#         ws["E3"].alignment = Alignment(horizontal="center", vertical = "center")
#         ws["E3"].border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
#                                      top = Side(border_style="thin"), bottom = Side(border_style="thin"))
#         ws["E3"].fill = PatternFill(start_color="66CFCC", end_color = "66CFCC", fill_type = "solid")
#         ws['E3'].font = Font(name = 'Calibro', size = 10, bold = True)
#         ws['E3'] = 'Total'
            
#             #pintamos los datos
            
            
#         ws.cell(row = controlador, column = 2).alignment = Alignment(horizontal = "center") #cell son celdas
#         ws.cell(row = controlador, column = 2).border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
#                                     top = Side(border_style = "thin"), bottom = Side(border_style = "thin") )
#         ws.cell(row = controlador, column = 2).font = Font(name = 'Calibri', size = 8)
#         ws.cell(row = controlador, column = 2).value = user_str
            
#         ws.cell(row = controlador, column = 3).alignment = Alignment(horizontal = "center") #cell son celdas
#         ws.cell(row = controlador, column = 3).border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
#                                     top = Side(border_style = "thin"), bottom = Side(border_style = "thin") )
#         ws.cell(row = controlador, column = 3).font = Font(name = 'Calibri', size = 8)
#         ws.cell(row = controlador, column = 3).value = factura.descripcion
            
#         ws.cell(row = controlador, column = 5).alignment = Alignment(horizontal = "center") #cell son celdas
#         ws.cell(row = controlador, column = 5).border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
#                                     top = Side(border_style = "thin"), bottom = Side(border_style = "thin") )
#         ws.cell(row = controlador, column = 5).font = Font(name = 'Calibri', size = 8)
#         ws.cell(row = controlador, column = 5).value = int(factura.total)
            
#         controlador += 1
#         cont += 1 #le da el numero a cada pagina
            
#         # Definir el rango de filas que deseas combinar
#         start_row = 1
#         end_row = 20

# # Combinar las celdas de las columnas C y D
#         for row in range(start_row, end_row + 1):
#             ws.merge_cells(start_row=row, start_column=3, end_row=row, end_column=4)
        
  

#         #Establecer el nombre de mi archivo
#         nombre_archivo = "ReportePersonalizadoExcel.xlsx"
#         #Definir el tipo de respuesta que se va a dar
#         response = HttpResponse(content_type = "application/ms-excel")
#         contenido = "attachment; filename = {0}".format(nombre_archivo)
#         response["Content-Disposition"] = contenido
#         wb.save(response)
#         return response
    
