from django.shortcuts import render, HttpResponse, redirect
from posts.models import *
from posts.forms import PostCreateForm, CommentCreateForm
from users.utils import get_user_from_request
# Create your views here.

def main(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        data = {
            'posts': posts
        }
        return render(request, 'layouts/main.html', context=data)

PAGINATION_LIMIT = 4

def post_view(request):
    if request.method == 'GET':
        hashtag_id = request.GET.get('hashtag_id')
        search_text = request.GET.get('search')
        page=int(request.GET.get('page', 1))
        if hashtag_id:
            posts = Post.objects.filter(hashtag=Hashtag.objects.get(id=hashtag_id))
        else:
            posts = Post.objects.all()

        if search_text:
            posts = posts.filter(title__icontains=search_text)

        max_page = round(posts.__len__() / PAGINATION_LIMIT)
        posts = posts[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]


        data = {
            'posts': posts,
            'user': get_user_from_request(request),
            'hashtag': hashtag_id,
            'max_page': range(1, max_page+1)

        }

        return render(request, 'posts/posts.html', context=data)


def hash_view(request):
    if request.method == 'GET':
        context = {'hashtags': Hashtag.objects.all(),
                   'user': get_user_from_request(request)
                   }
        return render(request, 'hashtag/hashtag.html', context=context)

def post_detail_view(request, **kwargs):
    if request.method == 'GET':
        post = Post.objects.get(id=kwargs['id'])
        data = {
            'post':post,
            'comments': Comment.objects.filter(post_id=kwargs['id']),
            'form': CommentCreateForm,
            'user':get_user_from_request(request)
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
                'form': CommentCreateForm,
                'users': get_user_from_request(request)
            }
            return render(request, 'posts/detail.html', context=data)


def posts_create_view(request):
    if request.method == 'GET':
        data = {
            'form': PostCreateForm,
            'user': get_user_from_request(request)
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
            'form': form,
            'user': get_user_from_request(request)
            }
            return render(request, 'posts/create.html', context=data)