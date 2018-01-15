from django.shortcuts import render, redirect
from .models import Recipe
from django.http import JsonResponse
from django.core import serializers
from django import forms
# Create your views here.

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'image_path', 'description']

def get_recipes_api(request):
    recipes = Recipe.objects.all()
    data = serializers.serialize('json', recipes)
    return JsonResponse({'data': data})

def get_recipe(request, recipe_id):
    print(recipe_id)
    return render(request, 'recipe.html')


def get_create_recipe(request):
    return render(request, 'create_recipe.html')

def post_create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            new_recipe = form.save()
            print(new_recipe)
            return redirect('/')
        else:
            return redirect('/recipe/create')


