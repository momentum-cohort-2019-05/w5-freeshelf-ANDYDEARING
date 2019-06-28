from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from core.models import Book, Category, Favorite
from core.forms import FavoriteButtonForm, CommentCreateForm

# Create your views here.
class BookListView(generic.ListView):
    model = Book

def all_books(request):
    sort_types = ['added_at', 'author', 'title',]
    
    sort_by = request.GET.get('sort_by', default='added_at')
    if sort_by not in sort_types:
        sort_by = 'added_at'

    book_list = Book.objects.all().order_by(sort_by)
    
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

    return render(request, 'core/category_list.html', {
        'book_list': book_list,
        'sort_by': sort_by,
        'sort_types': sort_types,
        'category_name': category_name
     })

def favorites(request,pk):
    sort_types = ['added_at', 'author', 'title',]
    user_name = User.objects.get(id=pk).username
    sort_by = request.GET.get('sort_by', default='added_at')
    if sort_by not in sort_types:
        sort_by = 'added_at'

    # need to figure out the logic and syntax here
    book_list = []
    # for book in request.user.favorite_set.all:
    #     book_list.append(book)
    fave_list = request.user.favorite_set.all()
    for favorite in fave_list:
        book_list.append(favorite.favorite_book)

    return render(request, 'core/favorites.html', {
        'user_name': user_name,
        'book_list': book_list,
        'sort_by': sort_by,
        'sort_types': sort_types,
     })

def book_detail(request,pk):
    if request.method == 'POST':
        form = FavoriteButtonForm(request.POST)
        if form.is_valid():
            favorited = form.cleaned_data['favorited']
            book = Book.objects.get(pk=pk)
            if favorited:
                new_fav = Favorite(user=request.user,favorite_book=book)
                book.times_favorited += 1
                book.save()
                new_fav.save()
            else:
                old_fav = Favorite.objects.filter(user=request.user).filter(favorite_book=book).first()
                book.times_favorited -= 1
                book.save()
                old_fav.delete()

        return redirect(to='book-detail', pk=pk)

    else:            
        form = FavoriteButtonForm()
        book = Book.objects.get(pk=pk)
        fave_list = book.favorite_set.all()
        favorite_users=[]
        for favorite in fave_list:
            favorite_users.append(favorite.user)
        return render(request, 'core/book_detail.html', {
            'book' : book,
            'favorite_users' : favorite_users,
            'form' : form
        })

def make_comment(request,pk):
    if request.method == 'POST':
        pass
    else:
        form = CommentCreateForm()
        book = Book.objects.get(pk=pk)

        return render(request, 'core/comment.html', {
            'book' : book,
            'form' : form,
        })

