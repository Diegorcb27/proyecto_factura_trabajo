from django.urls import path
from .views import FacturaCreateView, FacturaListView, FacturaDetailView, FacturaUpdateView, FacturaDeleteView, generate_pdf, ReportePersonalizadoExcel

facturas_patterns = ([
    path('', FacturaListView.as_view(), name="facturas_list"),
    path('create/', FacturaCreateView.as_view(), name="facturas_create"),
    path('update/<int:pk>/', FacturaUpdateView.as_view(), name="facturas_update"),
    path('delete/<int:pk>/', FacturaDeleteView.as_view(), name="facturas_delete"),
    path('detail/<int:pk>/', FacturaDetailView.as_view(), name="facturas_detail"),
    path('generate_pdf/<int:pk>/', generate_pdf, name='facturas_pdf'),
    path('reporte/<int:pk>/', ReportePersonalizadoExcel.as_view(), name="reporte")
    

    
], "facturas")