from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import Factura, Cliente
from .forms import FacturaForm
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from django.shortcuts import redirect

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
class FacturaCreateView(CreateView): #el staffRequiredMixin que le pasamos como parametro es para comprobar si el usuario ha iniciado sesion para poder usar el create, 
    model = Factura
    form_class=FacturaForm
    # fields = ["descripcion", "total", "usuario"]
    # success_url = reverse_lazy('facturas:facturas_list') #me redirecciona a la lista de las facturas
    def get_success_url(self):
        return reverse_lazy('facturas:facturas_list')
    
    
@method_decorator(login_required, name='dispatch')
class FacturaListView(ListView):
    model=Factura
    context_object_name = 'factura_list'
    template_name = 'factura_list.html'
    paginate_by=5
    
    def get_queryset(self): #ordena la factura por numero de factura
        return Factura.objects.all().order_by('-numero_factura')
  
           
    
    
@method_decorator(login_required, name='dispatch')
class FacturaUpdateView(UpdateView):
    model = Factura
    form_class=FacturaForm
    # fields = ["descripcion", "total"]
    template_name_suffix = "_update_form"
    
    def get_success_url(self):
      
        return reverse_lazy('facturas:facturas_list')
    
@method_decorator(login_required, name='dispatch')

class FacturaDeleteView(DeleteView):
    model = Factura
    success_url = reverse_lazy('facturas:facturas_list')
    

class FacturaDetailView(DetailView):
    model = Factura
    
#creando cliente



#generar PDF

from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from .models import Factura
from django.views.generic.list import ListView
import tempfile

def generate_pdf(request, pk):
#     factura = Factura.objects.get(pk=pk)
#     template = get_template('facturas/factura_detail_pdf.html')
#     context = {
#         "descripcion": factura.descripcion,
#         "total": factura.total,
#         "id": factura.id,
#         "usuario": factura.usuario
#     }
#     html_template = template.render(context)
#     pdf_file = HTML(string=html_template).write_pdf()

#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'filename="factura_{pk}.pdf"'
#     response['Content-Transfer-Encoding'] = 'binary'

#     with tempfile.NamedTemporaryFile(delete=True) as output:
#         output.write(pdf_file)
#         output.flush()

#         output = open(output.name, 'rb')
#         response.write(output.read())

#     return response
    
    
    # try:
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
    
    # f' attachment; filename="factura_{pk}.pdf"'
    # except Exception as e:
    #     return HttpResponse(f"Error: {e}")
    
    #generar Excel
from openpyxl import Workbook
from openpyxl.styles import Alignment,Border,Font,PatternFill,Side



class ReportePersonalizadoExcel(TemplateView):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        factura = Factura.objects.get(id=pk)
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
    
