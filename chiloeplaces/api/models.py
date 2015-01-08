from django.db import models

class Lugares(models.Model):
    nombre = models.CharField(max_length=140)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)
    ubicacion = models.ForeignKey('Ubicacion')
    creado_por = models.ForeignKey('User')
    fecha = models.DateTimeField()

class ubicacion(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()


