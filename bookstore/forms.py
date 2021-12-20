from django import forms
from django.db.models import fields
from . import models

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = [
            'title',
            'description',
            'image'
        ]

class CommentBookForm(forms.ModelForm):
    class Meta:
        model = models.CommentBook
        fields = [
            'post',
            'text',
        ]