from django.shortcuts import render

from App1.forms import *
from App1.models import *

def inicio(request):
    return render(request,'index.html')




def suscripcionForm(request):
    if request.method== 'POST':
        persona = SuscripcionFormulario(request.POST)
        print(persona)

        if persona.is_valid:
            informacion = persona.cleaned_data

            usuario = Suscripcion (nombreSuscripcion= informacion['nombreSuscripcion'], apellidoSuscripcion = informacion['apellidoSuscripcion'], emailSuscripcion = informacion['emailSuscripcion'],)
            usuario.save()
        return render(request, 'index.html')
    
    else:
        persona = SuscripcionFormulario()
    return render(request, 'App1/suscripcion.html', {'persona':persona})


def prestamosForm(request):
    if request.method== 'POST':
        prestamo = PrestamoFormulario(request.POST)
        print(prestamo)

        if prestamo.is_valid:
            informacion = prestamo.cleaned_data

            pedido = Prestamo(nombre= informacion['nombre'], apellido = informacion['apellido'], dni=informacion['dni'],fecha=informacion['fecha'],
            genero = informacion['genero'],situacion = informacion['situacion'], banco = informacion['banco'],email = informacion['email'],
            telefono = informacion['telefono'], cantidad = informacion['cantidad'],)
            pedido.save()
        return render(request, 'index.html')
    
    else:
        prestamo = PrestamoFormulario()
    return render(request, 'App1/prestamo.html', {'prestamo':prestamo})


def leerSuscriptores(request):
    suscriptores= Suscripcion.objects.all()
    contexto={'suscriptores':suscriptores}

    return render(request, 'App1/leerSuscriptores.html', contexto)
    
