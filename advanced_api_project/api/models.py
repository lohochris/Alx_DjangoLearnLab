from django.db import models

"""
Models for the API:
1. Author - Represents an author with a name field.
2. Book - Represents a book with title, publication year, and a foreign key to Author.
"""

class Author(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """Model representing a book written by an author."""
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
