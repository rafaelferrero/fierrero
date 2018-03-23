# -*- coding: UTF-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from entidades.choices import (
    CUIT_CUIL,
)


class Persona(models.Model):
    codigo_id = models.CharField(
        max_length=10,
        verbose_name=_("CUIT o CUIL"),
        choices=CUIT_CUIL,
        default=CUIT_CUIL[0][0],
    )
    numero_id = models.CharField(
        max_length=20,
        verbose_name=_("Número de CUIT/CUIL"),
    )

    def __str__(self):
        try:
            if hasattr(self, 'persona'):
                return "{0}".format(self.fisica.nombre_completo)
            elif hasattr(self, 'compania'):
                return "{0}".format(self.juridica.nombre_completo)
        except NotImplementedError:
            return _("ERROR! esto no es ni una persona ni una compañía")
