from django.shortcuts import redirect, render
from .models import Product
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm



def home(request):
    products = Product.objects.all()  # Отримуємо всі товари
    return render(request, 'store/home.html', {'products': products})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'store/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})
