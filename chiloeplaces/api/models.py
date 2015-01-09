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
    estado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'{0}'.format(self.nombre)

    class Meta:
        verbose_name_plural = "Lugares"

class Ubicacion(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()
    lugar = models.OneToOneField('Lugar')

    def __unicode__(self):
		return u'{0},{1}'.format(self.latitud, self.longitud)

class Comuna(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(blank=True, max_length=140, null=True)

	def __unicode__(self):
		return u'{0}'.format(self.nombre)

class Imagenes(models.Model):
    url = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=300, blank=True)
    lugar = models.ForeignKey('Lugar', related_name='imagenes', null=True)

    def __unicode__(self):
		return u'{0}'.format(self.url)


class Actividad(models.Model):
    nombre = models.CharField(max_length=140)
    direccion = models.CharField(max_length=140)
    descripcion = models.CharField(max_length=300)
    valor = models.IntegerField(blank=True)
    fecha_inicio = models.DateTimeField(blank=True)
    fecha_termino = models.DateTimeField(blank=True)
    lugar = models.CharField(max_length=140)
    comuna = models.OneToOneField(Comuna)

    def __unicode__(self):
        return u'{0}'.format(self.nombre)

