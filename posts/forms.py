from django import forms
from posts.models import Hashtag

HASHTAG_CHOICES = (
    (hashtag.id, hashtag.title) for hashtag in Hashtag.objects.all()
)

class PostCreateForm(forms.Form):
    title = forms.CharField(max_length=10)
    descripition = forms.CharField(widget=forms.Textarea)
    price = forms.IntegerField()
    rate = forms.FloatField()

class CommentCreateForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Введите комментарий')

class HashtagCreateView(forms.Form):
    title = forms.CharField(max_length=10)