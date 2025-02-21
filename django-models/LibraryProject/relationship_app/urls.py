from django.urls import path
from . import views  # Import views from the same directory

urlpatterns = [
    path('', views.home, name='home'),  # Home view
    path('books/', views.list_books, name='list_books'),  # List books
    path('register/', views.register_view, name='register'),  # Registration
    path('login/', views.login_view, name='login'),  # Login
    path('logout/', views.logout_view, name='logout'),  # Logout
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),

    # New Paths for Book Management
    path('books/add/', views.add_book, name='add_book'),  # Add book
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book'),  # Edit book
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),  # Delete book
]
