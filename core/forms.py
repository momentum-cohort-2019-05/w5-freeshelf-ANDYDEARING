from django import forms
from core.models import Book, Favorite, Comment, Category, BookSuggestion

class FavoriteButtonForm(forms.Form):
    favorited = forms.BooleanField(required=False)

class CommentCreateForm(forms.Form):
    content = forms.CharField(max_length=1000)

class BookForm(forms.Form):
    title = forms.CharField(max_length=200)
    author = forms.CharField(max_length=200)
    url = forms.URLField()
    description = forms.CharField(max_length=1000)
    image_url = forms.URLField()
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

class CategoryCreateForm(forms.Form):
    category = forms.CharField(max_length=200)

class BookSuggestionForm(forms.Form):
    title = forms.CharField(max_length=200)
    author = forms.CharField(max_length=200)
    url = forms.CharField()
    description = forms.CharField(max_length=1000)
    image_url = forms.CharField()
    suggested_categories = forms.CharField(max_length=1000)