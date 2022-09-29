from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SuscripcionFormulario(forms.Form):
    nombreSuscripcion = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}) )
    apellidoSuscripcion = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido'}) )
    emailSuscripcion = forms.EmailField( widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'E-Mail'}) )
    contraSuscripcion = forms.CharField(max_length=40 , widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Contraseña'}))
    
class PrestamoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}))
    apellido = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido'}))
    dni=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'D.N.I'}))
    fecha=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'placeholder':'Fecha Nacimiento'}))
    genero = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Genero'}))
    situacion = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Situacion (E.j: Monotributista)'}))
    banco = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Banco (E.j: Santander)'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'E-Mail'}))
    telefono = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Telefono'}))
    cantidad = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cantidad solicitada: '}))
    




