# -*- coding: utf-8 -*-

from os.path import abspath
from piston.handler import BaseHandler

from rh.servidor.models import Servidor

class ServidorHandler(BaseHandler):
    allowed_methods = ("GET",)
    
    def read(self, request, **kwargs):

        operacao = kwargs['operacao']

        if operacao == 'criar':
            s = Servidor.objects.create(user=kwargs['user'], nome=kwargs['nome'], email=kwargs['email'])
        elif operacao == 'alterar':
            s = Servidor.objects.get(id=kwargs['id'])
            s.user = kwargs['user']
            s.nome = nome=kwargs['nome']
            s.email = kwargs['email']
            s.save()
        elif operacao == 'buscar':
            s = Servidor.objects.get(id=kwargs['id'])
        elif operacao == 'excluir':
            s = Servidor.objects.get(id=kwargs['id'])
            s.delete()
            return "EXCLUIDO!"
        elif operacao == 'listar':
            s = Servidor.objects.all()
            return s
        return s.__dict__
