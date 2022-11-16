from django.urls import path
from posts import views

urlpatterns = [
    path('posts/', views.post_view)
]