from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from ..models import Category, Ingredient


class CategoryNode(DjangoObjectType):

    class Meta:
        model = Category
        exclude_fields = ['ingredients']
        interfaces = [relay.Node]
        filter_fields = []


class IngredientNode(DjangoObjectType):

    class Meta:
        model = Ingredient
        interfaces = [relay.Node]
        filter_fields = ['category__name']


class IngredientQuery(object):
    all_categories = DjangoFilterConnectionField(CategoryNode)
    all_ingredients = DjangoFilterConnectionField(IngredientNode)
