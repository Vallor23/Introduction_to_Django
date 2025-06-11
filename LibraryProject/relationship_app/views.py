from django.shortcuts import render
from .models import Book, Library

# Create your views here.
def book_list(request):
     """Retrieves all books and renders a template displaying the list."""
     books = Book.objects.all()  # Fetch all book instances from the database
     return render(request, context={'book_list': books})  # Rebder context dictionary with book list
