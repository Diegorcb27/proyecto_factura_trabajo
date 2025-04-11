from django.urls import path
from .views import ProductoCreateView, ProductoListView, ProductoUpdateView, ProductoDeleteView,  ProductoDetailView

productos_patterns = ([
    path('', ProductoListView.as_view(), name="productos_list"),
    path('create/', ProductoCreateView.as_view(), name="productos_create"),
    path('update/<int:pk>/', ProductoUpdateView.as_view(), name="productos_update"),
    path('delete/<int:pk>/', ProductoDeleteView.as_view(), name="productos_delete"),
    path('detail/<int:pk>/', ProductoDetailView.as_view(), name="productos_detail"),

    
], "productos")