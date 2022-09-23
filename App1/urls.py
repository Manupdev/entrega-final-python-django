from django.urls import path 
from App1.views import *

urlpatterns = [
    path('',inicio),
    path('prestamo/', prestamosForm),
    path('suscripcion/', suscripcionForm),
    path('leerSusc/', leerSuscriptores),
]
