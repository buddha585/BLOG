from django.urls import path
from posts import views

urlpatterns = [
    path('posts/', views.post_view),
    path('hashtags/', views.HashtagView.as_view()),
    path('posts/<int:id>/',  views.post_detail_view),
    path('posts/create/', views.PostsCreateView.as_view())

]