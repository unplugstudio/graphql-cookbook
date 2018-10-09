import django_filters

from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from ..models import Category, Ingredient


# Filters

class IngredientFilterSet(django_filters.FilterSet):
    category = django_filters.CharFilter('category__name', lookup_expr='exact')

    class Meta:
        model = Ingredient
        fields = ['category']


# Types

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


class IngredientQuery(object):
    all_categories = DjangoFilterConnectionField(CategoryNode)
    all_ingredients = DjangoFilterConnectionField(
        IngredientNode, filterset_class=IngredientFilterSet)
