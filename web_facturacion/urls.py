"""
URL configuration for web_facturacion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.urls import core_patterns
from facturas.urls import facturas_patterns
from Cliente.urls import cliente_patterns
from Productos.urls import productos_patterns
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core_patterns)),
    path('facturas/', include(facturas_patterns) ),
    path('cliente/', include(cliente_patterns) ),
    path('productos/', include(productos_patterns) ),
    #Path de Auth
    path('accounts/', include('django.contrib.auth.urls')), #agrega todas las urls necesarias para el inicio de sesion de un usuario
    path('accounts/', include('registration.urls')) #esto es para registrar el usuario
    
    
]

#debemos resolver la carga de los ficheros media

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)