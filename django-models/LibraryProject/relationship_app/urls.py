from django.urls import path
from . import views  # Import views from the same directory
from .views import LibraryDetailView, list_books, add_book, edit_book, delete_book
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Home View
    path('', views.home, name='home'),

    # Authentication and Registration
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),  # Custom Login View
    path('logout/', views.logout_view, name='logout'),  # Custom Logout View

    # User Role-Based Views
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),

    # Book Management
    path('books/', list_books, name='list_books'),  # List all books
    path('add_book/', add_book, name='add_book'),  # Add a new book
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),  # Edit an existing book
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),  # Delete a book

    # Library Detail View
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication Views (Alternative)
    path('auth/login/', LoginView.as_view(template_name='relationship_app/login.html'), name='auth_login'),
    path('auth/logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='auth_logout'),
]
