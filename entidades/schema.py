# -*- coding: UTF-8 -*
from graphene_django import DjangoObjectType
import graphene
from entidades.models import Fisica, Juridica


class SchemaPersonaFisica(DjangoObjectType):
    class Meta:
        model = Fisica


class SchemaPersonaJuridica(DjangoObjectType):
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
