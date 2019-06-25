from django.shortcuts import render
from django.views import generic
from core.models import Book

# Create your views here.
class BookListView(generic.ListView):
    model = Book