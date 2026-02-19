from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipelist.html"


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes.html"