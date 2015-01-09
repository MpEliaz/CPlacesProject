from rest_framework import serializers
from models import *

class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagenes
        fields = ('id', 'url', 'descripcion', 'lugar')

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = ('id', 'latitud', 'longitud', 'lugar')

class LugarSerializer(serializers.ModelSerializer):

    imagenes = serializers.StringRelatedField(many=True, read_only=True)
    ubicacion = UbicacionSerializer(read_only=True)
    comuna = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Lugar
        fields = ('id', 'nombre', 'direccion', 'telefono', 'comuna', 'descripcion', 'creado_por', 'fecha', 'imagenes', 'ubicacion')

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ('id', 'nombre', 'descripcion')

class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ('id', 'nombre', 'descripcion', 'valor', 'fecha_inicio', 'fecha_termino', 'lugar', 'comuna')

