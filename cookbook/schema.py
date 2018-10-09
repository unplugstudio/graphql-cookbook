import graphene

from recipes.schema.ingredients import IngredientQuery
from recipes.schema.recipes import RecipeQuery


class Query(IngredientQuery, RecipeQuery, graphene.ObjectType):
    hello = graphene.Field(graphene.String)

    def resolve_hello(self, info, **kwargs):
        user = info.context.user
        if user.is_authenticated:
            return "Hello %s!" % user
        return "Hello stranger"


schema = graphene.Schema(query=Query)
