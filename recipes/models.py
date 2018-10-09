from django.db import models


class Category(models.Model):
    """
    A group for several ingredients.
    """
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """
    An ingredient.
    """
    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    category = models.ForeignKey(Category, related_name='ingredients', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """
    A simple recipe.
    """
    title = models.CharField(max_length=100)
    instructions = models.TextField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class RecipeElement(models.Model):
    """
    A record of an Ingredient used in a Recipe.
    """
    recipe = models.ForeignKey(Recipe, related_name='elements', on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, related_name='elements', on_delete=models.CASCADE)
    amount = models.FloatField()
    unit = models.CharField(max_length=20, choices=(
        ('unit', 'Units'),
        ('kg', 'Kilograms'),
        ('l', 'Litres'),
        ('st', 'Shots'),
    ))

    def __str__(self):
        return str(self.ingredient)
