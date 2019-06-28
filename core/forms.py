from django import forms
from core.models import Book, Favorite, Comment

class FavoriteButtonForm(forms.Form):
    favorited = forms.BooleanField(required=False)

class CommentCreateForm(forms.Form):
    content = forms.CharField(max_length=1000)