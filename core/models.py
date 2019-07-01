from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-books', args=[str(self.id)])

class BookSuggestion(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000, null=True)
    image_url = models.CharField(max_length=1000, null=True)
    suggested_categories = models.CharField(max_length=1000, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = [ 'title' ]

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    url = models.URLField(unique=True)
    description = models.TextField(max_length=1000)
    added_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(null=True)
    category = models.ManyToManyField(Category)
    times_favorited = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = [ 'added_at', 'title']
        permissions = (('can_add_edit_delete',"Add/Edit/Delete Books"),)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    favorited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}|{self.favorite_book}"

    class Meta:
        unique_together = [ 'user', 'favorite_book' ]
        ordering = [ '-favorited_at']

class Comment(models.Model):
    """Model representing a comment"""
    content = models.TextField(max_length=1000, help_text='Enter your comment (1000 chars max).')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    target_book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """sorts by the reverse of the post_date"""
        ordering = [ '-created_at' ]

    def __str__(self):
        """String for representing the Model object."""
        return self.content