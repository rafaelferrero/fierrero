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
            if hasattr(self, 'fisica'):
                return "{0}".format(self.fisica.nombre_completo)
            elif hasattr(self, 'juridica'):
                return "{0}".format(self.juridica.nombre_completo)
            else:
                return "{}:{}".format(self.codigo_id, self.numero_id)
        except NotImplementedError:
            return _("ERROR! esto no es ni una persona ni una compañía")


class Fisica(Persona):
    nombre = models.CharField(
        max_length=150,
        verbose_name=_("Nombre"),
    )
    segundo_nombre = models.CharField(
        max_length=150,
        verbose_name=_("Segundo Nombre"),
        null=True,
        blank=True,
    )
    tercer_nombre = models.CharField(
        max_length=150,
        verbose_name=_("Tercr Nombre"),
        null=True,
        blank=True,
    )
    apellido = models.CharField(
        max_length=150,
        verbose_name=_("Apellido"),
    )
    segundo_apellido = models.CharField(
        max_length=150,
        verbose_name=_("Segundo Apellido"),
        null=True,
        blank=True,
    )
    tercer_apellido = models.CharField(
        max_length=150,
        verbose_name=_("Tercer Apellido"),
        null=True,
        blank=True,
    )

    @property
    def nombre_completo(self):
        return "{}, {}".format(
            self.apellido.upper(),
            self.nombre
        )

    def __str__(self):
        return self.nombre_completo


class Juridica(Persona):
    razon_social = models.CharField(
        max_length=150,
        verbose_name=_("Razón Social")
    )

    @property
    def nombre_completo(self):
        return "{}".format(
            self.razon_social
        )

    def __str__(self):
        return self.nombre_completo
