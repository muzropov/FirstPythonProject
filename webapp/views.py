from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    return render(request, 'post/index.html')

def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'post/home.html', context)

