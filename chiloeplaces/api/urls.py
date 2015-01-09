from django.conf.urls import patterns, include, url
from rest_framework import routers
from rest_framework.routers import SimpleRouter
from views import *

routers = SimpleRouter()
routers.register(r'lugares', LugarViewSet)
routers.register(r'imagenes', ImagenesViewSet)
routers.register(r'comunas', ComunaViewSet)
routers.register(r'ubicaciones', UbicacionViewSet)
routers.register(r'actividades', ActividadViewSet)
urlpatterns = patterns('', url(r'^api/', include(routers.urls)),
)
