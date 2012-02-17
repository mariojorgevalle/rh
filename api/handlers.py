# -*- coding: utf-8 -*-

from os.path import abspath
from piston.handler import BaseHandler

from rh.servidor.models import Servidor

class ServidorHandler(BaseHandler):
    allowed_methods = ("GET",)
    
    def read(self, request, **kwargs):
        if 'id' in kwargs:
            s = Servidor.objects.get(id=kwargs['id'])
        else:
            s = Servidor.objects.create(user=kwargs['user'], nome=kwargs['nome'], email=kwargs['email'])
        return s.__dict__
