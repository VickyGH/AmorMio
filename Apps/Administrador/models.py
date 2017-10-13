from __future__ import unicode_literals

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

# class Imagen(models.Model):
#    img = models.FilePathField()
#    fecha = models.DateField()
#    persona = models.ManyToManyField(Personas)
#    detalle = models.CharField(max_length=250, default=False)
#    tag = models.ManyToManyField(Tags)
