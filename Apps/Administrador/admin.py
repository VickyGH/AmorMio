from django.contrib import admin

from .models import *
# Register your models here.
class TagsAdmin(admin.ModelAdmin):
    fields = ['nombre']

class PersonasAdmin(admin.ModelAdmin):
    fields = ['nombre','apellidos', 'alias', 'foto']

class ImagenesAdmin(admin.ModelAdmin):
    filter=['fechaSubida']

admin.site.register(Tags, TagsAdmin)
admin.site.register(Personas, PersonasAdmin)
admin.site.register(Imagenes,ImagenesAdmin)