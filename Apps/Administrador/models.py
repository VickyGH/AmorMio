from __future__ import unicode_literals

from datetime import datetime
from django.db import models


# Choices

# Create your models here.
class Tags(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Tags"


class Personas(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=60)
    alias = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='pic_person/%Y/%m/%d', default='pic_person/None/no-img.jpg')

    def __unicode__(self):
        return '%s %s %s' % (self.nombre, self.apellidos, self.alias)

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Personas"

class Imagenes(models.Model):
    imagen = models.ImageField(upload_to='fotos/%Y/%m/%d', default='fotos/None/no-img.jpg', verbose_name='Fotografia')
    fechaSubida = models.DateTimeField(default=datetime.now(), verbose_name='Fecha de Imagen')
    fechaCaptura = models.DateTimeField(default=datetime.now(), verbose_name='Fecha Tomada')
    personasFoto = models.ManyToManyField(Personas,verbose_name='Personas en la fotografia')
    personaUser=models.CharField(max_length=250, verbose_name='Usuario')
    detalle = models.CharField(max_length=250, default='Sin detalles', verbose_name='Hastag')
    tag = models.ManyToManyField(Tags)

    def __unicode__(self):
        return '%s' % (self.detalle)

    class Meta:
        ordering = ["fechaSubida"]
        verbose_name_plural = "Imagenes"
