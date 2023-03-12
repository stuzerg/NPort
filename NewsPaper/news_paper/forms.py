from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets, Textarea, RadioSelect, Select

from .models import Post, Category
from django_filters import ModelMultipleChoiceFilter


class PostForm(forms.ModelForm):

   class Meta:
       model = Post
       fields = ['cat', 'author', 'header', 'body'
       ]

# class CategoryForm(forms.ModelForm):
#
#    class Meta:
#        model = Category
#        fields = ["name", "subscribers"]
