from django.contrib import admin
from entidades.models import Juridica, Fisica


@admin.register(Juridica)
class PersonaJuridicaAdmin(admin.ModelAdmin):
    pass


@admin.register(Fisica)
class PersonaFisicaAdmin(admin.ModelAdmin):
    pass
