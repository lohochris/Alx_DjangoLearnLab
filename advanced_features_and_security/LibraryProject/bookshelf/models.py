from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from accounts.models import CustomUser as BaseCustomUser

User = get_user_model()

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField(default=timezone.now)
    isbn = models.CharField(max_length=13, unique=True)  # Unique ISBN field
    summary = models.TextField(blank=True, null=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='books_added')

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_publish_books", "Can publish books"),
            ("can_archive_books", "Can archive books"),
            ("can_edit_books", "Can edit book details"),
        ]
        ordering = ['-published_date']

    def __str__(self):
        return self.title


# Proxy model for CustomUser
class CustomUser(BaseCustomUser):
    class Meta:
        proxy = True

