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
    if request.method == 'GET':
        context = {'posts': Post.objects.all()}
        return render(request, 'posts/posts.html', context=context)

def hash_view(request):
    if request.method == 'GET':
        context = {'hashtags': Hashtag.objects.all()}
        return render(request, 'hashtag/hashtag.html', context=context)
