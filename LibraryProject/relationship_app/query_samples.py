from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Book, Library

# Filtering books by author
def  get_book_by_author(author):
      get_book_by_author = Book.objects.filter(author__name=author)
      return get_book_by_author

# Retrieving all books
def get_books_in_library(library_name):
    library =  Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a library.
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian