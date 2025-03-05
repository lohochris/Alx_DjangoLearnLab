from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList  # Ensure BookList is imported

# Create a router and register the ViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),  # This will include /api/books/
    path('books-list/', BookList.as_view(), name='book-list'),  # Add BookList view
]
