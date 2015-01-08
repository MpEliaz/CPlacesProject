from rest_framework import serializers
from models import *


class LugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugar
        fields = ('id', 'nombre', 'direccion', 'telefono', 'descripcion', 'creado_por', 'fecha')

