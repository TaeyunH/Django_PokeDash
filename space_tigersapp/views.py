from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product


def landing(request):
    return render(request, 'landing.html')  


def index(request):
    product_list = Product.objects.all()  
    return render(request, 'index.html', {'products': product_list})  


def new(request):
    return HttpResponse('New Page')  


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) 
        if form.is_valid():
            form.save()  
            return redirect('login') 
    else:
        form = UserCreationForm()  
    return render(request, 'signup.html', {'form': form})  