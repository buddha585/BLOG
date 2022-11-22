from django.shortcuts import render
from posts.models import *
from django.http import HttpResponse
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

def post_detail_view(request, **kwargs):
    if request.method == 'GET':
        post = Post.objects.get(id=kwargs['id'])
        data = {
            'post':post,
            'comments': Comment.objects.filter(post_id=kwargs['id'])
        }

        return render(request, 'posts/details.html', context=data)
