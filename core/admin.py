from django.contrib import admin
from core.models import Book, Category, Favorite

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Favorite)