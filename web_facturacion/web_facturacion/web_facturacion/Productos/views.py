from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Productos
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required 
from .forms import ProductoForm
from django.utils import timezone


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


