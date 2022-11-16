from django.shortcuts import render
from posts.models import *
# Create your views here.

def main(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        data = {
            'posts': posts
        }
        return render(request, 'layouts/main.html', context=data)

def post_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        data = {
            'posts': posts
        }
        return render(request, 'posts.html', context=data)