from django.db import models
from django.contrib.auth.models import User

class Lugar(models.Model):
    nombre = models.CharField(max_length=140)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50)
    comuna = models.ForeignKey('Comuna')
    descripcion = models.CharField(max_length=300)
    creado_por = models.ForeignKey(User)
    fecha = models.DateTimeField(auto_now=True)

class Ubicacion(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()
    lugar = models.ForeignKey('Lugar')

class Comuna(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(blank=True, max_length=140, null=True)

	def __unicode__(self):
		return u'{0}'.format(self.nombre)



