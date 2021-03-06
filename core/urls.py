from django.urls import path
from . import views

urlpatterns = [
        # path('', views.BookListView.as_view(), name='home'),
        path('', views.all_books, name='home'),
        path('category/<int:pk>', views.category_books, name='category-books'),
        path('favorites/<int:pk>', views.favorites, name='favorites'),
        path('book-detail/<int:pk>', views.book_detail, name='book-detail'),
        path('make-comment/<int:pk>', views.make_comment, name='make-comment'),
        path('user-profile/<int:pk>', views.user_profile, name='user-profile'),
        path('staff', views.staff_page, name='staff'),
        path('edit-book/<int:pk>', views.edit_book, name='edit-book'),
        path('delete-book/<int:pk>', views.delete_book, name='delete-book'),
        path('add-book', views.add_book, name='add-book'),
        path('suggestions', views.suggestions, name='suggestions'),
        path('approve-suggestion/<int:pk>', views.approve_suggestion, name='approve-suggestion'),
        path('delete-suggestion/<int:pk>', views.delete_suggestion, name='delete-suggestion'),
        path('make-category', views.make_category, name='make-category'),
        path('delete-confirm/<int:pk>', views.delete_confirm, name='delete-confirm')
]