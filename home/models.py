from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    hobbies = models.TextField()


# Create your models here.
