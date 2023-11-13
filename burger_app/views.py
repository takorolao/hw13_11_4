from django.shortcuts import render, redirect
from .models import Burger, Ingredient
from .forms import BurgerForm

def burger_list(request):
    burgers = Burger.objects.all()
    ingredients = Ingredient.objects.all()
    return render(request, 'burger_app/burger_list.html', {'burgers': burgers, 'ingredients': ingredients})


def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'burger_app/ingredient_list.html', {'ingredients': ingredients})


def create_burger(request):
    if request.method == 'POST':
        form = BurgerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('burger_list')
    else:
        form = BurgerForm()

    return render(request, 'burger_app/create_burger.html', {'form': form})