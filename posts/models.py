from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    price = models.FloatField()
    rate = models.DecimalField(max_digits=10, decimal_places=1)
    hashtags = models.ManyToManyField('Hashtag', blank=True)
    def str(self):
        return self.title

class Hashtag(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    posts = models.ManyToManyField(Post, blank=True)
    def str(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.author.username}_{self.text}'