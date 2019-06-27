from django.urls import path
from . import views

urlpatterns = [
        # path('', views.BookListView.as_view(), name='home'),
        path('', views.all_books, name='home'),
        path('category/<int:pk>', views.category_books, name='category-books'),
        path('favorites/<int:pk>', views.favorites, name='favorites'),
        path('book-detail/<int:pk>', views.book_detail, name='book-detail'),
]