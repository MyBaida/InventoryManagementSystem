from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login_view')
def index(request):
    return render(request, 'index.html')


@login_required(login_url='login_view')
def order(request):
    return render(request, 'order.html')


@login_required(login_url='login_view')
def product(request):
    product = Product.objects.all()

    form = ProductForm(request.POST or None)
    if form.is_valid():
        name = request.POST.get('name')
        form.save()
        messages.success(request, f"'{name}' has been added")
        return redirect('product_view')

    context = {
        'product' : product,
        'form' : form
    }
    return render(request, 'product.html', context)


@login_required(login_url='login_view')
def staff(request):
    return render(request, 'staff.html')


@login_required(login_url='login_view')
def edit(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductEditForm(request.POST or None, instance=product)
    if form.is_valid():
        name = request.POST.get('name')
        form.save()
        messages.warning(request, f"'{name}' has been updated")
        return redirect('product_view')

    context = {
        'form' : form
    }

    return render(request, 'edit.html', context)


@login_required(login_url='login_view')
def delete(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        name = product.name
        product.delete()
        messages.error(request, f"'{name}' has been deleted")
        return redirect('product_view')
    return render(request, 'delete.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('home_view')
    
    form = CreateUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home_view')
    
    context = {
        'form' : form,
    }
    return render(request, 'register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home_view')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_view')
        
        messages.warning(request, "Username or Password is invalid")
        return redirect('login_view')
    return render(request, 'login.html')


@login_required(login_url='login_view')
def logout_view(request):
    logout(request)
    messages.success(request, "You have logged out successfully")
    return redirect('login_view')
