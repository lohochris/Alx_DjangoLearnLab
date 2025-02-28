from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model  # Import the custom user model correctly
from django.db.models.signals import post_save
from django.dispatch import receiver

# Get the custom user model
User = get_user_model()

class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ('can_add_book', 'Can add book'),
            ('can_change_book', 'Can change book'),
            ('can_delete_book', 'Can delete book'),
            ('can_view_book', 'Can view book'),  # Added custom permission for viewing
        ]

class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

    class Meta:
        permissions = [
            ('can_view_library', 'Can view library'),  # Custom permission for viewing
            ('can_create_library', 'Can create library'),  # Custom permission for creating
            ('can_edit_library', 'Can edit library'),  # Custom permission for editing
            ('can_delete_library', 'Can delete library'),  # Custom permission for deleting
        ]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Use the custom user model
    role = models.CharField(max_length=20, choices=[
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member')
    ])

    def __str__(self):
        return self.user.email  # Assuming your custom user model uses email as username

# Signal to create a UserProfile when a new User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
