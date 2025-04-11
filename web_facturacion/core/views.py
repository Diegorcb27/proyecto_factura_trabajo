from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.

class HomePageView(TemplateView):
    template_name = "core/home.html"
    
    def get(self, request, *args, **kwargs): #esto es para pasar la informacion al template
        return render(request, self.template_name, {'title': "Llevamos todas tus facturas al dia"})
    

