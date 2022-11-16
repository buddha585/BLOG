from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    price = models.FloatField()
    rate = models.DecimalField(max_digits=10, decimal_places=1)

class Hashtag(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
