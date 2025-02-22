from django.urls import path
from . import views  # Import views from the same directory
from .views import LibraryDetailView
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('', views.home, name='home'),  # Home view
    path('books/', views.list_books, name='list_books'),  # List books
    path('register/', views.register_view, name='register'),  # Registration
    path('login/', views.login_view, name='login'),  # Login
    path('logout/', views.logout_view, name='logout'),  # Logout
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
    path('books/', list_books, name='list_books'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # New Paths for Book Management
    path('books/add/', views.add_book, name='add_book'),  # Add book
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book'),  # Edit book
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),  # Delete book
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
   

]
