from .models import Recipe, RecipeImage
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .forms import RecipeForm, ImageForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipelist.html"


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipes.html"


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'recipeadd.html'
    form_class = RecipeForm


class RecipeImageView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    template_name = 'recipeimage.html'
    form_class = ImageForm

    def get_success_url(self):
        return reverse_lazy('ledger:recipe_detail',
                            kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.recipe_id = self.kwargs['pk']
            form.save()
        return redirect(self.get_success_url())
