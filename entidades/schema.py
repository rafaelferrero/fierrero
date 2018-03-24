# -*- coding: UTF-8 -*
from graphene_django import DjangoObjectType
import graphene
from entidades.models import Persona


class SchemaPersona(DjangoObjectType):
    class Meta:
        model = Persona


class Query(graphene.ObjectType):
    personas = graphene.List(SchemaPersona)

    def resolve_personas(self, info):
        return Persona.objects.all()


schema = graphene.Schema(query=Query)
