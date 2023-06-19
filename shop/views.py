from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def homeshop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'onetomany/shop/home.html', {'products': products, 'categories': categories})

def createCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeshop')
    else:
        form = CategoryForm()
    return render(request, 'onetomany/shop/createcategory.html', {'form': form})

def createProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeshop')
    else:
        form = ProductForm()
    return render(request, 'onetomany/shop/createproduct.html', {'form': form})
