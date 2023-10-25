from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('plan/', views.plan, name='plan'),
    path('food/', views.food, name='food'),
    path('training', views.training, name='training'),
    path('FAQ/', views.FAQ, name='FAQ'),
    
    
]