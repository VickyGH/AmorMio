from __future__ import unicode_literals

from django import forms

class AgregarPersonaForm(forms.Form):
    """Image upload form."""
    nombre = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    alias = forms.CharField(max_length=50)
    foto = forms.ImageField(label='Selecciona una Imagen')

class AgregarTagsForm(forms.Form):
    nombre = forms.CharField(max_length=50)