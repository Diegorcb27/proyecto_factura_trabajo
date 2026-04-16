from django.urls import path
from .views import FacturaCreateView, FacturaListView, FacturaDetailView, FacturaUpdateView, FacturaDeleteView, ProductoListView, ProductoCreateView, ProductoDeleteView, ProductoDetailView, ProductoUpdateView,ClienteCreateView, ClienteListView, ClienteUpdateView, ClienteDeleteView, ClienteDetailView, PartnerAddressCreateView, PartnerAddressUpdateView, PartnerAddressDeleteView, PartnerAddressDetailView,  ContactoCreateView, ContactoDeleteView, ContactoUpdateView, FacturasTransactionsCreateView, FacturasTransactionsUpdateView, FacturasTransactionDeleteView, facturas_por_cliente, contacto_por_cliente, generate_pdf, direccion_por_cliente, generate_pdf, ReportePersonalizadoExcel

facturas_patterns = ([
    path('', FacturaListView.as_view(), name="facturas_list"),
    path('create/', FacturaCreateView.as_view(), name="facturas_create"),
    path('update/<int:pk>/', FacturaUpdateView.as_view(), name="facturas_update"),
    path('delete/<int:pk>/', FacturaDeleteView.as_view(), name="facturas_delete"),
    path('detail/<int:pk>/', FacturaDetailView.as_view(), name="facturas_detail"),
    path('generate_pdf/<int:pk>/', generate_pdf, name='facturas_pdf'),
    path('reporte/<int:pk>/', ReportePersonalizadoExcel.as_view(), name="reporte"),
    ], "facturas")

productos_patterns = ([
    path('', ProductoListView.as_view(), name="productos_list"),
    path('create/', ProductoCreateView.as_view(), name="productos_create"),
    path('update/<int:pk>/', ProductoUpdateView.as_view(), name="productos_update"),
    path('delete/<int:pk>/', ProductoDeleteView.as_view(), name="productos_delete"),
    path('detail/<int:pk>/', ProductoDetailView.as_view(), name="productos_detail"),
    ], "productos")

cliente_patterns = ([
    path('', ClienteListView.as_view(), name="cliente_list"),
    path('create/', ClienteCreateView.as_view(), name="cliente_create"),
    path('update/<int:pk>/', ClienteUpdateView.as_view(), name="cliente_update"),
    path('delete/<int:pk>/', ClienteDeleteView.as_view(), name="cliente_delete"),
    path('detail/<int:pk>/', ClienteDetailView.as_view(), name="cliente_detail" ),
   
    #Direccion del cliente
    path('adress/cliente/create/<int:partner_id>/', PartnerAddressCreateView.as_view(), name="adress_cliente_create"),
    path('adress/cliente/update/<int:pk>/', PartnerAddressUpdateView.as_view(), name="adress_cliente_update"),
    path('adress/cliente/delete/<int:pk>/', PartnerAddressDeleteView.as_view(), name="adress_cliente_delete"),
    path('adress/cliente/detail/<int:pk>/', PartnerAddressDetailView.as_view(), name="adress_cliente_detail"),
    path('adress/cliente/<int:cliente_id>/', direccion_por_cliente, name="direccion_por_cliente"),
    #generacion de documentos
    path('facturas/cliente/<int:cliente_id>/', facturas_por_cliente, name='facturas_por_cliente'),
    path('facturas/cliente/<int:cliente_id>/generate_pdf/<int:pk>/', generate_pdf, name='facturas_pdf'),
    # path('', ContactoListView.as_view(), name='contacto_list'),
    path('contacto/create/<int:cliente_id>/', ContactoCreateView.as_view(), name="contacto_create"),
    path('contacto_update/<int:pk>/', ContactoUpdateView.as_view(), name="contacto_update"),
    path('contacto_delete/<int:pk>/', ContactoDeleteView.as_view(), name="contacto_delete"),
    path('contacto/cliente/<int:cliente_id>/', contacto_por_cliente, name='contacto_por_cliente'),
    ], "cliente")


transaction_patterns = ([
    # path('', FacturaListView.as_view(), name="facturas_list"),
    path('create/<int:product_id>/', FacturasTransactionsCreateView.as_view(), name="transaction_create"),
    path('update/<int:pk>/', FacturasTransactionsUpdateView.as_view(), name="transaction_update"),
    path('delete/<int:pk>/', FacturasTransactionDeleteView.as_view(), name="transaction_delete"),
   
    ], "transaction")