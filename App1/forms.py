from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SuscripcionFormulario(forms.Form):
    nombreSuscripcion = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}) )
    apellidoSuscripcion = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido'}) )
    emailSuscripcion = forms.EmailField( widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'E-Mail'}) )
    dniSuscripciones1 = forms.IntegerField()
    
class PrestamoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni=forms.IntegerField()
    fecha=forms.DateField()
    genero = forms.CharField(max_length=20)
    situacion = forms.CharField(max_length=20)
    banco = forms.CharField(max_length=40)
    email = forms.EmailField()
    telefono = forms.IntegerField()
    cantidad = forms.IntegerField()
    

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contrasñea', widget=forms.PasswordInput)

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']
        help_text = {k:"" for k in fields}


