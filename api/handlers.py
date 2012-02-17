# -*- coding: utf-8 -*-

from os.path import abspath
from piston.handler import AnonymousBaseHandler, BaseHandler

from rh.servidor.models import Servidor
from rh.servidor.forms import FormServidor

class ServidorHandler(BaseHandler):
    allowed_methods = ("GET", "POST", "DELETE", "PUT")
    model = Servidor

    def read(self, request, servidor_id=None):
#        import pdb; pdb.set_trace()
        if servidor_id:
            return Servidor.objects.get(pk=servidor_id)
        else:
            return Servidor.objects.all()

#    @validate(ServidorForm)
    def create(self, request, **kwargs):
#        import pdb; pdb.set_trace()
#        if request.post:
#            data = request.data
#            
#            em = self.model(nome=data['nome'], user=data['user'], email=data['email'])
#            em.save()
#            
#            return rc.CREATED
#        else:
#            super(ExpressiveTestModel, self).create(request)
        pass

    def delete(self, resquest, id):
        pass

#    @validate(FormServidor, "PUT")
    def update(self, request):
#        import pdb; pdb.set_trace()
        pass
