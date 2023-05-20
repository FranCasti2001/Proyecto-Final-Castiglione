from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from ckeditor.fields import RichTextFormField

class CreacionDeUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contrasenia", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contrasenia", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
        
class EdicionDeUsuario(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(label = 'Nombre', max_length = 20)
    last_name = forms.CharField(label = 'Apellido', max_length = 20)
    descripcion = RichTextFormField()
    avatar = forms.ImageField(required = False)
    
    class Meta:
     model = User
     fields = ['email', 'first_name', 'last_name', 'descripcion', 'avatar']
            
class BuscarPaleta(forms.Form):
     
    nombre = forms.CharField (max_length = 30, required = False)