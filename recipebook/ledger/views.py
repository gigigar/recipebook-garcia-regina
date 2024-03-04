from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Recipe


# Create your views here.

class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'

class RecipeDetailsView(DetailView):
    model = Recipe
    template_name = 'ledger/recipe_details.html'