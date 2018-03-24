from django.contrib import admin
from entidades.models import Persona


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    pass
