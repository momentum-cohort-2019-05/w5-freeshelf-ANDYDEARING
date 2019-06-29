from django.contrib import admin
from core.models import Book, Category, Favorite, Comment, BookSuggestion

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Favorite)
admin.site.register(Comment)
admin.site.register(BookSuggestion)
