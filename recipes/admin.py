from django.contrib import admin

from .models import Recipe, RecipeElement, Category, Ingredient


class RecipeElementInline(admin.TabularInline):
    model = RecipeElement


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeElementInline]
    list_display = ['title', 'featured']
    list_editable = ['featured']


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    list_editable = ['name', 'category']


admin.site.register(Category)
