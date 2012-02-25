# -*- coding: utf-8 -*-

from os.path import abspath
from piston.handler import AnonymousBaseHandler, BaseHandler

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
        if request.post:
            data = request.data
            
            novo_servidor = self.model(nome=data['nome'], user=data['user'], email=data['email'])
            novo_servidor.save()
            
            return rc.CREATED
        return "ERRO!"

    def delete(self, request):
        data = request.data
        
        servidor = self.model.get(pk=data['servidor_id'])
        servidor.delete()

        return "APAGADO"

    def update(self, request):
        data = request.data
        
        servidor = self.model.get(pk=data['servidor_id'])
        servidor.nome=data['nome']
        servidor.user=data['user']
        servidor.email=data['email']
        servidor.save()
        
        return "ATUALIZADO"

