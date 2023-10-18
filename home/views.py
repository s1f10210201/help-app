# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'home/index.html')

def update(request, article_id):
    return HttpResponse("article_id: {}".format(article_id))

# Create your views here.
