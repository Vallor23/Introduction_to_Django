from django.shortcuts import render, redirect
from .models import Book, Library
from django.views.generic import DetailView
from django.views import View
from django.contrib.auth.forms import UserCreationForm

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

# Autentication Views
class RegisterView(View):
    def get(self, request):
     form = UserCreationForm()
     return render(request,'relationship_app/register.html',{'form':form})
    
    def post(self, request):
     form= UserCreationForm(request.POST)
     if form.is_valid():
          form.save()  #creates and saves te new user
          return redirect('login')  # Redirect to login page after successful registartion
     return render(request,'relationship_app/register.html',{'form':form})