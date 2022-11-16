from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    price = models.FloatField()
    rate = models.DecimalField(max_digits=10, decimal_places=1)
    def str(self):
        return self.title
class Hashtag(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    def str(self):
        return self.title

# class Review(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models