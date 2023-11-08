from django.apps import AppConfig
from django import forms
# from .models import UserProfile


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['name', 'age', 'grade', 'location', 'hobbies']