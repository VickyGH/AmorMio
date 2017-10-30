from __future__ import unicode_literals

from django import forms

from .models import Personas, Tags


class AgregarPersonaForm(forms.Form):
    """Image upload form."""
    nombre = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    alias = forms.CharField(max_length=50)
    foto = forms.ImageField(label='Selecciona una Imagen')

class AgregarTagsForm(forms.Form):
    nombre = forms.CharField(max_length=50)

class AgregarImagenesForm(forms.Form):
    class Meta:
        model = Tags, Personas
    imagen = forms.ImageField(label='Fotografia ')
    #fechaSubida = forms.DateTimeField()
    #fechaCaptura = forms.DateTimeField()
    personasFoto = forms.ModelMultipleChoiceField(queryset=Personas.objects.all(), label='Personas en la Fotografia ')
    personaUser = forms.CharField(max_length=250, label='Usuario ')
    detalle = forms.CharField(max_length=250, label='Detalle ')
    tag = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(), label='Hastag ')
