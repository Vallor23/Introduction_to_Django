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
        permissions = [
            ('can_add_book', 'Can add book'),
            ('can_change_book', 'Can change book'),
            ('can_delete_book', 'Can delete book'),
        ]
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
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(choices=ROLE_CHOICES, max_length=10, default='member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# signal to automatically create a UserProfile when a new user is registered.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)