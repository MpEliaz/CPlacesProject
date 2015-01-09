from rest_framework import serializers
from models import *

class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagenes
        fields = ('id', 'url', 'descripcion', 'lugar')

class LugarSerializer(serializers.ModelSerializer):

    imagenes = ImagenSerializer(many=True, read_only=True)
    class Meta:
        model = Lugar
        fields = ('id', 'nombre', 'direccion', 'telefono', 'comuna', 'descripcion', 'creado_por', 'fecha', 'imagenes')

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ('id', 'nombre', 'descripcion')



