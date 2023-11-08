from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserProfile
from .form import UserProfileForm

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

# def profile(request):
#     user_profile = UserProfile.objects.first()  # ここでは最初のプロフィールを取得しています
#     form = UserProfileForm(instance=user_profile)

#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, instance=user_profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')

#     return render(request, 'profile.html', {'user_profile': user_profile, 'form': form})



