from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    url = models.URLField(unique=True)
    description = models.TextField(max_length=1000)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [ 'added_at', 'title']

    def __str__(self):
        return self.title