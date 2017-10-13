from django.contrib import admin

from .models import *
# Register your models here.
class TagsAdmin(admin.ModelAdmin):
    fields = ['nombre']

class PersonasAdmin(admin.ModelAdmin):
    fields = ['nombre', 'foto']

admin.site.register(Tags, TagsAdmin)
admin.site.register(Personas, PersonasAdmin)