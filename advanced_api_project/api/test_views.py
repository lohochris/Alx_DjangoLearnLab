from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(TestCase):
    """
    Test case for the Book API endpoints, including CRUD operations, 
    filtering, searching, and ordering.
    """

    def setUp(self):
        """Set up test data and API client."""
        self.client = APIClient()

        # Create a test user for authentication
        self.user = User.objects.create_user(username="testuser", password="testpassword")

        # Create test books
        self.book1 = Book.objects.create(title="Python Crash Course", author="Eric Matthes", publication_year=2019)
        self.book2 = Book.objects.create(title="Django for Beginners", author="William S. Vincent", publication_year=2020)
        self.book3 = Book.objects.create(title="Machine Learning Guide", author="John Doe", publication_year=2021)

    def test_get_books_list(self):
        """Test retrieving the list of books."""
        response = self.client.get(reverse("book-list"), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 3)

    def test_get_single_book(self):
        """Test retrieving a single book by ID."""
        response = self.client.get(reverse("book-detail", kwargs={"pk": self.book1.pk}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["title"], self.book1.title)

    def test_create_book(self):
        """Test creating a new book (authentication required)."""
        self.client.force_authenticate(user=self.user)  # Simulate an authenticated request
        data = {
            "title": "Deep Learning",
            "author": "Ian Goodfellow",
            "publication_year": 2018
        }
        response = self.client.post(reverse("book-list"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    def test_update_book(self):
        """Test updating an existing book (authentication required)."""
        self.client.force_authenticate(user=self.user)
        updated_data = {"title": "Updated Python Course", "author": "Eric M.", "publication_year": 2022}
        response = self.client.put(reverse("book-detail", kwargs={"pk": self.book1.pk}), updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Python Course")

    def test_delete_book(self):
        """Test deleting a book (authentication required)."""
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(reverse("book-detail", kwargs={"pk": self.book2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)

    def test_filter_books(self):
        """Test filtering books by title (if enabled in filters)."""
        response = self.client.get(reverse("book-list") + "?search=Python Crash Course", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        books = response.json()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]["title"], "Python Crash Course")

    def test_search_books(self):
        """Test searching books by author name (if enabled in filters)."""
        response = self.client.get(reverse("book-list") + "?search=Vincent", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        books = response.json()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]["author"], "William S. Vincent")

    def test_order_books_by_title(self):
        """Test ordering books by title in ascending order."""
        response = self.client.get(reverse("book-list") + "?ordering=title", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        books = response.json()
        titles = [book["title"] for book in books]
        self.assertEqual(titles, sorted(titles))  # Ensure sorting order is correct

    def test_order_books_by_publication_year_desc(self):
        """Test ordering books by publication year in descending order."""
        response = self.client.get(reverse("book-list") + "?ordering=-publication_year", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        books = response.json()
        years = [book["publication_year"] for book in books]
        self.assertEqual(years, sorted(years, reverse=True))  # Ensure sorting order is correct
