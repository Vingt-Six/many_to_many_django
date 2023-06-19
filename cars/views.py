from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    cars = Car.objects.all()
    colors = Color.objects.all()
    return render(request, 'onetomany/cars/home.html', {'cars': cars, 'colors': colors})

def createColor(request):
    if request.method == 'POST':
        form = ColorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ColorForm()
    return render(request, 'onetomany/cars/createcolor.html', {'form': form})

def createCar(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CarForm()
    return render(request, 'onetomany/cars/createcar.html', {'form': form})

def destroy(request, id):
    delete = Color.objects.get(id=id)
    delete.delete()
    return redirect('home')