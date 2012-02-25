from django.conf.urls.defaults import *
from piston.resource import Resource
from rh.api.handlers import ServidorHandler

class CsrfExemptResource( Resource ):
	def __init__( self, handler, authentication = None ):
		super( CsrfExemptResource, self ).__init__( handler, authentication )
		self.csrf_exempt = getattr( self.handler, 'csrf_exempt', True )

servidor_handler = Resource(ServidorHandler)

urlpatterns = patterns('',
    url(r'^servidores/(?P<emitter_format>.+)/$', servidor_handler),
#    url(r'^servidor/$', servidor_handler, { 'emitter_format': 'json' }),
    url(r'^servidor/(?P<servidor_id>.+)/(?P<emitter_format>.+)/$', servidor_handler),
    url(r'^servidor/$', servidor_handler),
    url(r'^servidor/$', servidor_handler),
    url(r'^servidor/$', servidor_handler),
)
