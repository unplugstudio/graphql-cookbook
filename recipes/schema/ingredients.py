import graphene
from graphene_django.types import DjangoObjectType

from ..models import Category, Ingredient


class CategoryNode(DjangoObjectType):

    class Meta:
        model = Category
        exclude_fields = ['ingredients']


class IngredientNode(DjangoObjectType):

    class Meta:
        model = Ingredient


class IngredientQuery(object):
    all_categories = graphene.List(CategoryNode)
    all_ingredients = graphene.List(IngredientNode, category=graphene.String())

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_ingredients(self, info, **kwargs):
        category = kwargs.get('category')
        if category is None:
            return Ingredient.objects.all()
        return Ingredient.objects.filter(category__name=category)
