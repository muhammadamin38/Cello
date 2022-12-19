from django.shortcuts import render
from core.views import *
from .models import Post

def iop(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request ,  'index.html')
