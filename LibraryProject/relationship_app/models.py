from datetime import timezone
from django.db import models

# Create your models here
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=13, null=True, blank=True)
    publication_year = models.DateField(default=timezone.utc)
    class Meta:
        ordering = ['-publication_year']
    
    def __str__(self):
        return f"{self.title} by {self.author}" 
    
class Library(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book, related_name='books')
    
    def __str__(self):
        return f"{self.name}" 
    
class Librarian(models.Model):
    name = models.CharField(max_length=50)
    ibrary = models.OneToOneField(Library, on_delete=models.CASCADE,  related_name='librarian')
    
    def __str__(self):
        return f"{self.name} of {self.library}" 