from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient

# Register your models here.

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    
class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        RecipeIngredientInline,
    ]

class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)    