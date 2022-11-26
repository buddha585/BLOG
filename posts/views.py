from django.shortcuts import render, HttpResponse, redirect
from posts.models import *
from posts.forms import PostCreateForm, CommentCreateForm
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
        hashtag_id = request.GET.get('hashtag_id')
        if hashtag_id:
            posts = Post.objects.filter(hashtag=Hashtag.objects.get(id=hashtag_id))
        else:
            posts = Post.objects.all()
        context = {
            'posts': posts
        }
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
            'comments': Comment.objects.filter(post_id=kwargs['id']),
            'form': CommentCreateForm
        }

        return render(request, 'posts/details.html', context=data)
    if request.method == 'POST':
        form = CommentCreateForm(data=request.POST)

        if form.is_valid():
            Comment.objects.create(
                author_id=2,
                text=form.cleaned_data.get('text'),
                post_id=kwargs['id']
            )
            return redirect(f'/posts/{kwargs["id"]}/')
        else:
            post = Post.objects.get(id=kwargs['id'])
            comment = Comment.objects.filter(post=post)

            data = {
                'post': product,
                'comments': comment,
                'form': CommentCreateForm
            }
            return render(request, 'posts/detail.html', context=data)


def posts_create_view(request):
    if request.method == 'GET':
        data = {
            'form': PostCreateForm
        }
        return render(request, 'posts/create.html', context=data)
    if request.method == 'POST':
        form = PostCreateForm(data=request.POST)

        if form.is_valid():
            Post.objects.create(
            title=form.cleaned_data.get('title'),
            description=form.cleaned_data.get('description'),
            rate=form.cleaned_data.get('rate'),
            price = form.cleaned_data.get('price'),
            hashtag=form.cleaned_data.get('hashtag')
            )
            return redirect('/posts')
        else:
            data = {
            'form': form
            }
            return render(request, 'posts/create.html', context=data)