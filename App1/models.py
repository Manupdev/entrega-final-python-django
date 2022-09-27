from django.db import models

class Suscripcion(models.Model):
    nombreSuscripcion = models.CharField(max_length=40)
    apellidoSuscripcion = models.CharField(max_length=40)
    emailSuscripcion = models.EmailField()
    dniSuscripciones1 = models.IntegerField(blank=True, default = 0)

    def __str__(self):
        return self.nombreSuscripcion + "-" + self.apellidoSuscripcion + "-" + self.emailSuscripcion


class Prestamo(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni=models.IntegerField()
    fecha=models.DateField()
    genero = models.CharField(max_length=20)
    situacion = models.CharField(max_length=20)
    banco = models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.IntegerField()
    cantidad = models.IntegerField()


    def __str__(self):
        return self.nombre + "-" + self.apellido + "-" + self.dni
    
