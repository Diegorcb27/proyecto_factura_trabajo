from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como maximo y debe ser valido")
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
        #para que el email sea unico debemos hacer un metodo, debemos comprobar que el email no exista en la base de datos
    def clean_email(self):
        email = self.cleaned_data.get("email") #recuperamos el valor de clean o del email
        if User.objects.filter(email=email).exists(): #esto es para saber si existe, un usuario con ese email
            raise forms.ValidationError("El email ya esta registrado, prueba con otro") #como esta registrado levantara este error
        return email
    
#creamos el formulario para el perfil

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar", "bio", "link"] #esto es para editar los campos de profile
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}), #este widget es el que nos permite limpiar el campo
            'bio': forms.Textarea(attrs={'class': 'form-control mt-3', 'rows':3, 'placeholder':'Biografia'}),
            'link': forms.URLInput(attrs={'class': 'form-control mt-3', 'placeholder':'Enlace'})
        }
        
        
#creamos un formulario para editar el email del usuario
        
class EmailForm(forms.ModelForm):
    """Form definition for MODELNAME."""
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como maximo y debe ser valido")

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = User
        fields = ['email']
        
        #como no podemos ejar que el usuario coloque un email que ya existe copiamos el validado de clean email
    def clean_email(self):
        email = self.cleaned_data.get("email") #recuperamos el valor de clean o del email
        if 'email' in self.changed_data: #changed_data es una lista de todos los campos que se han editado en el formulario o se han añadido
            if User.objects.filter(email=email).exists(): #esto es para saber si existe, un usuario con ese email
                raise forms.ValidationError("El email ya esta registrado, prueba con otro") #como esta registrado levantara este error
        return email
    
            
            
        
    