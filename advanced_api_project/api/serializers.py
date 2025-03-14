from rest_framework import serializers
from .models import Author, Book
import datetime

"""
Serializers for transforming data between Django models and JSON format.

- BookSerializer:
  * Serializes Book model fields.
  * Includes validation to prevent future publication years.

- AuthorSerializer:
  * Serializes Author model fields.
  * Uses a nested BookSerializer to represent related books.
"""

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Includes validation to ensure publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """Ensure publication year is not in the future."""
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Includes a nested representation of related books.
    """
    books = BookSerializer(many=True, read_only=True)  # Nested serializer for books

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
