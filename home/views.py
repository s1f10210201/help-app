from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def profile(request):
    return render(request, 'home/profile.html')

def plan(request):
    return render(request, 'home/plan.html')

def food(request):
    return render(request, 'home/food.html')

def training(request):
    return render(request, 'home/training.html')

def FAQ(request):
    return render(request, 'home/FAQ.html')



