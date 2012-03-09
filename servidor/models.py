from django.db import models

class Servidor(models.Model):
    """
    """
    user = models.CharField(max_length=20)
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.nome

class Setor(models.Model):
    nome = models.CharField(max_length=50)
