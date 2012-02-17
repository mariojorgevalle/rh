from django.conf.urls.defaults import *
from rh.api.handlers import ServidorHandler
from piston.resource import Resource

servidor_handler = Resource(ServidorHandler)

urlpatterns = patterns('',
    (r'criar_servidor/(?P<user>.+)/(?P<nome>.+)/(?P<email>.+)/$', servidor_handler),
    (r'alterar_servidor/(?P<id>.+)/$', servidor_handler),
)
