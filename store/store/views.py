from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
import telegram
from .forms import RegisterForm
from .models import Product
from django.conf import settings

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def about(request):
    return render(request, 'about.html')


BOT_TOKEN = '7482287382:AAHhDKsslFgwuWPQFELMNAXJPgOpeWnNyE4'  
GROUP_ID = '-4604736800'  

async def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        text = f"📩 Новий запит із форми 'Contact Us':\n\n"
        text += f"👤 Ім'я: {name}\n"
        text += f"✉️ Email: {email}\n"
        text += f"💬 Повідомлення: {message}"


        bot = telegram.Bot(token=settings.BOT_TOKEN)
        
        await bot.send_message(chat_id=settings.GROUP_ID, text=text)


        return JsonResponse({'status': 'success', 'message': 'Thank you for contacting us!'})

    return render(request, 'contact.html')