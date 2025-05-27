from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.utils.dateparse import parse_date
from django.contrib.auth.decorators import login_required
from .models import Item, ShoppingCart
from .forms import CustomUserCreationForm
from django.contrib.auth import login

@login_required
def home(request):

    return render(request, "home.html")

def logout_now(request):
    return HttpResponse("<h1>Вы вышли из аккаунта</h1>Приходите ещё!")

def items(request):
    return HttpResponse("<h1>Эта страница ещё не готова, она появится позже.</h1>")

def items_card(request):
    return HttpResponse("<h1>Эта страница ещё не готова, она появится позже.</h1>")

def shopping_cart(request):

    carts = ShoppingCart.objects.all()
    total = 0
    
    for item in carts:
        total += item.item.price


    return render(request, "shopping_cart.html", {"carts":carts, "total":total})

def user(request):
    return HttpResponse("<h1>Эта страница ещё не готова, она появится позже.</h1>")


def items_list(request):

    items = Item.objects.all()

    return render(request, "items_list.html", {"items":items})

def product_list(request, item_id):

    product = Item.objects.get(id=item_id)

    return render(request, "product_list.html", {"product":product})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/login.html', {'form': form})
