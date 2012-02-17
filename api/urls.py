from django.conf.urls.defaults import *
from rh.api.handlers import ServidorHandler
from piston.resource import Resource

servidor_handler = Resource(ServidorHandler)

urlpatterns = patterns('servidor',
    (r'/(?P<operacao>.+)/(?P<id>.+)/(?P<user>.+)/(?P<nome>.+)/(?P<email>.+)/$', servidor_handler),
    (r'/(?P<operacao>.+)/(?P<user>.+)/(?P<nome>.+)/(?P<email>.+)/$', servidor_handler),
    (r'/(?P<operacao>.+)/(?P<id>.+)/$', servidor_handler),
    (r'/(?P<operacao>.+)/$', servidor_handler),
)
