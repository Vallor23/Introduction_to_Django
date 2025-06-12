from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=13, null=True, blank=True)
    publication_year = models.DateField(default=timezone.now)
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

class UserProfile(models.Model):
    ROLE_CHOICES =(
        ('admin','Admin'),
        ('librarian','Librarian'),
        ('member','Member')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', default='member')
    role = models.CharField(choices=ROLE_CHOICES, max_length=10)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# signal to automatically create a UserProfile when a new user is registered.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


















# Step 2: Set Up Role-Based Views

# Create three separate views to manage content access based on user roles:

#     Views to Implement:
#         An ‘Admin’ view that only users with the ‘Admin’ role can access, the name of the file should be admin_view
#         A ‘Librarian’ view accessible only to users identified as ‘Librarians’. The file should be named librarian_view
#         A ‘Member’ view for users with the ‘Member’ role, the name of the file should be member_view

#     Access Control:
#         Utilize the @user_passes_test decorator to check the user’s role before granting access to each view.

# Step 3: Configure URL Patterns

# Define URL patterns that will route to the newly created role-specific views. Ensure that each URL is correctly linked to its respective view and that the URLs are named for easy reference.

#     URLs to Define:
#         A URL for the ‘Admin’ view.
#         A URL for the ‘Librarian’ view.
#         A URL for the ‘Member’ view.

# Step 4: Create Role-Based HTML Templates

# For each role, create an HTML template to display relevant content when users access their respective views.