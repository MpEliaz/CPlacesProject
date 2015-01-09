from django.conf.urls import patterns, include, url
from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter
from views import *

routers = ExtendedSimpleRouter()
routers.register(r'lugares', LugarViewSet)
routers.register(r'imagenes', ImagenesViewSet)
routers.register(r'comunas', ComunaViewSet)
urlpatterns = patterns('', url(r'^api/', include(routers.urls)),
)
