# -*- coding: UTF-8 -*

import graphene
from graphene_django import DjangoObjectType
from entidades.models import Persona, Fisica, Juridica


class SchemaPersona(graphene.AbstractType):
    codigo_id = graphene.String()
    numero_id = graphene.String()


class SchemaPersonaFisica(DjangoObjectType, SchemaPersona):
    class Meta:
        model = Fisica


class SchemaPersonaJuridica(DjangoObjectType, SchemaPersona):
    class Meta:
        model = Juridica


class Query(graphene.ObjectType):
    personas_fisicas = graphene.List(SchemaPersonaFisica)
    personas_juridicas = graphene.List(SchemaPersonaJuridica)

    def resolve_personas_fisicas(self, info):
        return Fisica.objects.all()

    def resolve_personas_juridicas(self, info):
        return Juridica.objects.all()


schema = graphene.Schema(query=Query)
