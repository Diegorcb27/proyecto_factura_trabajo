from django.urls import path
from .views import ClienteCreateView, ClienteListView, ClienteUpdateView, ClienteDeleteView, facturas_por_cliente, generate_pdf
from facturas.views import ReportePersonalizadoExcel


cliente_patterns = ([
    path('', ClienteListView.as_view(), name="cliente_list"),
    path('create/', ClienteCreateView.as_view(), name="cliente_create"),
    path('update/<int:pk>/', ClienteUpdateView.as_view(), name="cliente_update"),
    path('delete/<int:pk>/', ClienteDeleteView.as_view(), name="cliente_delete"),
    path('facturas/cliente/<int:cliente_id>/', facturas_por_cliente, name='facturas_por_cliente'),
    path('facturas/cliente/<int:cliente_id>/generate_pdf/<int:pk>/', generate_pdf, name='facturas_pdf'),
    path('facturas/cliente/<int:cliente_id>/reporte/<int:pk>/', ReportePersonalizadoExcel.as_view(), name='reporte'),
    
  
  
    

    
], "cliente")