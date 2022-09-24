from django.shortcuts import render

from App1.forms import *
from App1.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

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



def login_request(request):

    if request.method == "POST":
        form =AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)


            if user is not None:
                login(request, user)

                return render(request, 'index.html', {'mensaje': f'Bienvenido {usuario}'})

            else:
                return render (request, 'index.html', {'mensaje': 'Error, datos incorrectos'})

        else:
                return render (request, 'index.html', {'mensaje': 'Error, formulario'})
    
    form = AuthenticationForm()

    return render(request, 'App1/login.html', {'form': form})



def register(request):

    if request.method == "POST":

        form= UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render (request, 'index.html' , {'mensaje': 'usuario creado'})
        
    else:
        form = UserRegisterForm()

    return render(request, 'App1/registro.html', {'form': form})


    
    
