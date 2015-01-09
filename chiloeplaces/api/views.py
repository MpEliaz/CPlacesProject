from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin
from serializers import *
# Create your views here.

class LugarViewSet(viewsets.ModelViewSet):
  queryset = Lugar.objects.all()
  serializer_class = LugarSerializer

class ImagenesViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
  queryset = Imagenes.objects.all()
  serializer_class = ImagenSerializer

class ComunaViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
  queryset = Comuna.objects.all()
  serializer_class = ComunaSerializer