from django import forms 

class SuscripcionFormulario(forms.Form):
    nombreSuscripcion = forms.CharField(max_length=40)
    apellidoSuscripcion = forms.CharField(max_length=40)
    emailSuscripcion = forms.EmailField()
    
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
    
