from django.contrib import admin
from core.models import Book, Category, Favorite, Comment

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Favorite)
admin.site.register(Comment)