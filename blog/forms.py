from django import forms
from django.forms import fields
from blog.models import Blog,Comment,Likes

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('comment',)