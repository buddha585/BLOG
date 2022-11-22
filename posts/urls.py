from django.urls import path
from posts import views

urlpatterns = [
    path('posts/', views.post_view),
    path('hashtags/', views.hash_view),
    path('posts/<int:id>/',  views.post_detail_view)
]