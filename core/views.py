from django.shortcuts import render
from django.views import generic
from core.models import Book, Category

# Create your views here.
class BookListView(generic.ListView):
    model = Book

def all_books(request):
    sort_types = ['added_at', 'author', 'title',]
    
    sort_by = request.GET.get('sort_by', default='added_at')
    if sort_by not in sort_types:
        sort_by = 'added_at'

    book_list = Book.objects.all().order_by(sort_by)
    
    # test_book = Book.objects.first()
    # breakpoint()

    return render(request, 'core/book_list.html', {
        'book_list': book_list,
        'sort_by': sort_by,
        'sort_types': sort_types,
     })

def category_books(request, pk):
    sort_types = ['added_at', 'author', 'title',]
    category_name = Category.objects.filter(id=pk).first().name
    sort_by = request.GET.get('sort_by', default='added_at')
    if sort_by not in sort_types:
        sort_by = 'added_at'

    book_list = Book.objects.filter(category__id=pk).order_by(sort_by)
    
    # test_book = Book.objects.first()
    # breakpoint()

    return render(request, 'core/category_list.html', {
        'book_list': book_list,
        'sort_by': sort_by,
        'sort_types': sort_types,
        'category_name': category_name
     })