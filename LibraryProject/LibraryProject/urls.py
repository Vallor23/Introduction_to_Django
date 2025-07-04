"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from bookshelf.views import BookListCreateAPIView
from relationship_app.views import LibraryDetailView, booklist_view, RegisterView, admin_view, librarian_view, member_view,add_book, delete_book, edit_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', BookListCreateAPIView.as_view(), name="book_list_create"),
    path('api/library/<int:pk>/', LibraryDetailView.as_view(), name="library_detail"),
    path('api/books/fbv/', booklist_view, name="book_list_fbv"),
    # Authentication urls
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    # Role based urls
    path('admin-only/', admin_view, name="admin_view"),
    path('librarian-only/', librarian_view, name="librarian_view"),
    path('member-only/', member_view, name="member_view"),
    # custom permission urls
    path('api/books/add_book/', add_book, name="add_book"),
    path('api/books/delete_book/<int:pk>/', delete_book, name="delete_book"),
    path('api/books/edit_book/<int:pk>/', edit_book, name="edit_book"),
]