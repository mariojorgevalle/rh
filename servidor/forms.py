# -*- coding:utf-8 -*-

from django import forms
from models import Servidor

class FormServidor(forms.ModelForm):
    class Meta:
        model = Servidor


