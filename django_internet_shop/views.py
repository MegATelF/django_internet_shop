from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.utils.dateparse import parse_date
from django.contrib.auth.decorators import login_required
from .models import Item, ShoppingCart
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout, authenticate

@login_required
def home(request):

    return render(request, "home.html")

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('items_list') 
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')  

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

@login_required
def items_list(request):

    items = Item.objects.all()

    return render(request, "items_list.html", {"items":items})

def product_list(request, item_id):

    product = Item.objects.get(id=item_id)

    return render(request, "product_list.html", {"product":product})

# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('items_list')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'accounts/registration.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # перенаправление на страницу входа после регистрации
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/registration.html', {'form': form})

# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = User(username=username)
#         user.set_password(password)  # хешируем пароль
#         user.save()
#         return redirect('login')
#     return render(request, 'accounts/registration.html')

# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         # Создаем пользователя с помощью create_user
#         user = User.objects.create_user(username=username, password=password)
#         # Можно сразу авторизовать или редиректить
#         return redirect('login')  # или куда нужно
#     return render(request, 'accounts/registration.html')