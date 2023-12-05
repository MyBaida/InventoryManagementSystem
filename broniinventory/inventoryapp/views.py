from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def order(request):
    return render(request, 'order.html')

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

def staff(request):
    return render(request, 'staff.html')

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

def delete(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        name = product.name
        product.delete()
        messages.error(request, f"'{name}' has been deleted")
        return redirect('product_view')
    return render(request, 'delete.html')
