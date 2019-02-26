from __future__ import unicode_literals
from django.conf import settings
from django.db import models



class Libro(models.Model):
    autor = models.CharField('Autor' ,max_length=142)
    nombre = models.CharField('Nombre',max_length=142)
   	datetime = models.DateTimeField('Fecha',auto_now=True)


class Persona(models.Model):
	nombre = models.CharField('Nombre', max_length=142)







