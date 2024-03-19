from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'

class RecipeDetailsView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe_details.html'