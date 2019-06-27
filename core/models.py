from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-books', args=[str(self.id)])




class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    url = models.URLField(unique=True)
    description = models.TextField(max_length=1000)
    added_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(null=True)
    category = models.ManyToManyField(Category)

    class Meta:
        ordering = [ 'added_at', 'title']

    def __str__(self):
        return self.title

