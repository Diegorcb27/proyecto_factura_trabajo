from django.urls import path
from .views import ClienteCreateView, ClienteListView, ClienteUpdateView, ClienteDeleteView, ClienteDetailView, ContactoCreateView, ContactoDeleteView, ContactoUpdateView, facturas_por_cliente, contacto_por_cliente, generate_pdf
from facturas.views import ReportePersonalizadoExcel


cliente_patterns = ([
    path('', ClienteListView.as_view(), name="cliente_list"),
    path('create/', ClienteCreateView.as_view(), name="cliente_create"),
    path('update/<int:pk>/', ClienteUpdateView.as_view(), name="cliente_update"),
    path('delete/<int:pk>/', ClienteDeleteView.as_view(), name="cliente_delete"),
    path('detail/<int:pk>/', ClienteDetailView.as_view(), name="cliente_detail" ),
    path('facturas/cliente/<int:cliente_id>/', facturas_por_cliente, name='facturas_por_cliente'),
    path('facturas/cliente/<int:cliente_id>/generate_pdf/<int:pk>/', generate_pdf, name='facturas_pdf'),
    # path('', ContactoListView.as_view(), name='contacto_list'),
    path('contacto/create/<int:cliente_id>/', ContactoCreateView.as_view(), name="contacto_create"),
    path('contacto_update/<int:pk>/', ContactoUpdateView.as_view(), name="contacto_update"),
    path('contacto_delete/<int:pk>/', ContactoDeleteView.as_view(), name="contacto_delete"),
    path('contacto/cliente/<int:cliente_id>/', contacto_por_cliente, name='contacto_por_cliente'),
   ], "cliente")