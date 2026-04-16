from django.contrib.auth.forms import UserCreationForm #aqui esta el formulario de registro
from django.shortcuts import get_object_or_404
from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView 
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required 
from .models import Profile
from django.urls import reverse_lazy
from django import forms
# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail #cambiamos el UserCreationForm por este otro que tiene un email
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    
    #Como queremos saber si un usuario se ha registrado bien y queremos mandar un mensaje,vamos a recuperar de la url un parametro que siga register
    
    def get_success_url(self):
        return reverse_lazy('login') + '?register' #esto manda el parametro register a la url de login, lo concatena
    
    #Esto es para recuperar e formulario y darle estilo en tiempo real
    def get_form(self, form_class =None):
        form = super(SignUpView, self).get_form()
        #Modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder': 'Nombre de usuario'})  #esto son los campos del formulario que se ven en la inspeccion
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder': 'Direccion email'})  
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder': 'Contraseña'})  #esto son los campos del formulario que se ven en la inspeccion
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder': 'Repite la contraseña'})  #esto son los campos del formulario que se ven en la inspeccion
        
        return form
    
#para poder entrar al perfil el usuario debe estar autenticado

@method_decorator(login_required, name="dispatch")
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy("profile")
    template_name = "registration/profile_form.html"
    
    def get_object(self):
        #recuperar el objeto a editar
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
    
# pagina para Actualizar email
@method_decorator(login_required, name="dispatch")
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy("profile")
    template_name = "registration/profile_email_form.html"
    
    #queremos recuperar el usuario
    def get_object(self):
        #recuperar el objeto a editar
        return self.request.user
    
    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form() #esto es para poder recuperar y modificar el formulario para que se vea mejor en tiempo real o tiempo de ejecucion
        #Modificar en tiempo real
        form.fields["email"].widget = forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Email'})
        return form
        
    
    

        
        

