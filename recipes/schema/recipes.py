import graphene

from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from ..models import Recipe, RecipeElement


class RecipeElementNode(DjangoObjectType):
    unit_display = graphene.String()

    class Meta:
        model = RecipeElement
        exclude_fields = ['recipe']
        interfaces = [relay.Node]

    def resolve_unit_display(self, info, **kwargs):
        return self.get_unit_display()


class RecipeNode(DjangoObjectType):

    class Meta:
        model = Recipe
        interfaces = [relay.Node]
        filter_fields = []


class RecipeQuery(object):
    recipe = relay.Node.Field(RecipeNode)
    all_recipes = DjangoFilterConnectionField(RecipeNode)
