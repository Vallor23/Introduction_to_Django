from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView

# Create your views here.
def booklist_view(request):
     """Retrieves all books and renders a template displaying the list."""
     books = Book.objects.all()  # Fetch all book instances from the database
     return render(request,'relationship_app/book_list.html', context={'book_list': books})  # Render context dictionary with book list

# Class based view
class LibraryDetailView(DetailView):
     model =  Library
     template_name = "relationship_app/library_detail.html"
     context_object_name = "library"