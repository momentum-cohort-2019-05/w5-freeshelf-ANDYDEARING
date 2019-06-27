from django import forms
from core.models import Book, Favorite

class FavoriteButtonForm(forms.Form):
    favorited = forms.BooleanField(required=False)