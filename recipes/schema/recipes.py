import graphene
from graphene_django.types import DjangoObjectType

from ..models import Recipe


class RecipeNode(DjangoObjectType):

    class Meta:
        model = Recipe


class RecipeQuery(object):
    all_recipes = graphene.List(RecipeNode)

    def resolve_all_recipes(self, info, **kwargs):
        return Recipe.objects.all()
