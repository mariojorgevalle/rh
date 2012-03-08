# -*- coding: utf-8 -*-

from os.path import abspath
from piston.handler import AnonymousBaseHandler, BaseHandler
from piston.utils import rc

from rh.servidor.models import Servidor
from rh.servidor.forms import FormServidor

class ServidorHandler(BaseHandler):
    allowed_methods = ("GET", "POST", "DELETE", "PUT")
    model = Servidor.objects

    def read(self, request, servidor_id=None):
        if servidor_id:
            return self.model.get(pk=servidor_id)
        else:
            return self.model.all()

    def create(self, request, **kwargs):
        data = request.data
        novo_servidor = self.model.create(nome=data['nome'], user=data['user'], email=data['email'])
        
        return rc.CREATED

    def delete(self, request, servidor_id=None):
        
        servidor = self.model.get(pk=servidor_id)
        servidor.delete()

        return rc.DELETED

    def update(self, request):
        data = request.data
        
        servidor = self.model.get(pk=data['servidor_id'])
        servidor.nome=data['nome']
        servidor.user=data['user']
        servidor.email=data['email']
        servidor.save()
        
        return rc.ALL_OK

