from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides full CRUD functionality for books,
    including filtering, searching, and ordering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Define permissions for different actions
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]  # Open for all users
        return [permissions.IsAuthenticated()]  # Restricted to authenticated users for create, update, delete

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering: Allow filtering by title, author, and publication_year
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Searching: Allow search on title and author's name
    search_fields = ['title', 'author__name']

    # Ordering: Allow ordering by title and publication_year
    ordering_fields = ['title', 'publication_year']
