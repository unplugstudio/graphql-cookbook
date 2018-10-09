import graphene

from recipes.schema.ingredients import IngredientQuery, IngredientMutation
from recipes.schema.recipes import RecipeQuery, RecipeMutation


class Query(IngredientQuery, RecipeQuery, graphene.ObjectType):
    hello = graphene.Field(graphene.String)

    def resolve_hello(self, info, **kwargs):
        user = info.context.user
        if user.is_authenticated:
            return "Hello %s!" % user
        return "Hello stranger"


class Mutation(IngredientMutation, RecipeMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
