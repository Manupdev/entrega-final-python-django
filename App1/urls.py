from django.urls import path 
from App1.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',inicio),
    path('prestamo/', prestamosForm),
    path('suscripcion/', suscripcionForm),
    path('leerSusc/', leerSuscriptores),
    path('login/',login_request),
    path('registro/', register),
    path('logout/', LogoutView.as_view(template_name = 'App1/logout.html')),
    
]
