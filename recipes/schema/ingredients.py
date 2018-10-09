import django_filters
import graphene

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


# Mutations

class AddIngredientMutation(relay.ClientIDMutation):

    class Input:
        name = graphene.String(required=True)
        notes = graphene.String()
        category = graphene.ID(required=True)

    ingredient = graphene.Field(IngredientNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        name = input.get('name')
        notes = input.get('notes', '')
        category_id = input.get('category')

        category = relay.Node.get_node_from_global_id(info, category_id)
        ingredient = Ingredient.objects.create(name=name, notes=notes, category=category)
        return cls(ingredient=ingredient)


class IngredientMutation(object):
    add_ingredient = AddIngredientMutation.Field()
