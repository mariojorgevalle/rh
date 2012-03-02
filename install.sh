#!/bin/bash
#Script de Instalação

sudo apt-get install python-dev libxml2
sudo apt-get install python-setuptools
easy_install pip

sudo pip install django==1.3
sudo pip install piston-django
sudo apt-get install python-django-piston python-piston-mini-client

python manage.py syncdb
python manage.py runserver 0.0.0.0:8080
