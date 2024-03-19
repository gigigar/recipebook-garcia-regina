from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile

# Register your models here.

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline,]

class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name']
    
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    
class UserAdmin(admin.BaseUserAdmin):
    inlines = [ProfileInlin,]

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin) 
admin.site.unregister(User)
admin.site.register(User, UserAdmin)   