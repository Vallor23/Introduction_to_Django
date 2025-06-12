from django.shortcuts import render, redirect
from .models import Book, Library, UserProfile
from django.views.generic import DetailView
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test

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


# check functions for the user’s role before granting access to each view
def is_admin(user):
     return hasattr(user, 'profile') and user.profile.role == 'admin'

def is_librarian(user):
     return hasattr(user, 'profile') and user.profile.role == 'librarian'

def is_member(user):
     return hasattr(user, 'profile') and user.profile.role == 'member'


# Role-Based Views to manage content access based on user roles
@user_passes_test(is_admin)
def admin_view(request):
     return render(request,'relationship_app/admin_view.html')

@user_passes_test(is_librarian) 
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
     return render(request,'relationship_app/member_view.html')