from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.detail import DetailView
from django.contrib.auth import views as auth_views  # Built-in authentication views

from .models import UserProfile, Book, Library
from .forms import BookForm

# Role Check Functions
def is_admin(user):
    """Check if user is an admin."""
    if user.is_authenticated:
        return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'
    return False

def is_librarian(user):
    """Check if user is a librarian."""
    if user.is_authenticated:
        return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'
    return False

def is_member(user):
    """Check if user is a member."""
    if user.is_authenticated:
        return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'
    return False

# Authentication Views using Django's Built-In Views
class CustomLoginView(auth_views.LoginView):
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True  # Redirects authenticated users

class CustomLogoutView(auth_views.LogoutView):
    next_page = 'login'

def logout_view(request):
    """Custom logout view."""
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login')

# Registration View
def register_view(request):
    """Handle user registration."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in user after registration
            messages.success(request, 'Account created successfully! You are now logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Book List View
@login_required
def list_books(request):
    """Display list of all books."""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def login_view(request):
    """Render the login page."""
    return render(request, 'relationship_app/login.html')

# Home View
@login_required
def home(request):
    """Render the home page."""
    return render(request, 'relationship_app/home.html')

# Admin View
@user_passes_test(is_admin, login_url='login')
def admin_view(request):
    """View accessible by admin users only."""
    return render(request, 'relationship_app/admin_view.html')

# Librarian View
@user_passes_test(is_librarian, login_url='login')
def librarian_view(request):
    """View accessible by librarians only."""
    return render(request, 'relationship_app/librarian_view.html')

class LibraryDetailView(DetailView):
    """Detail view for a library."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Member View
@user_passes_test(is_member, login_url='login')
def member_view(request):
    """View accessible by members only."""
    return render(request, 'relationship_app/member_view.html')

# Add Book View (Requires can_add_book permission)
@permission_required('relationship_app.add_book', raise_exception=True)
def add_book(request):
    """View for adding a book."""
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('list_books')
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

# Edit Book View (Requires can_change_book permission)
@permission_required('relationship_app.change_book', raise_exception=True)
def edit_book(request, book_id):
    """View for editing a book."""
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('list_books')
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

# Delete Book View (Requires can_delete_book permission)
@permission_required('relationship_app.delete_book', raise_exception=True)
def delete_book(request, book_id):
    """View for deleting a book."""
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})

# Library Detail View
def library_detail(request, library_id):
    """Detail view for a library and its books."""
    library = get_object_or_404(Library, id=library_id)
    books = library.books.all()
    return render(request, 'relationship_app/library_detail.html', {'library': library, 'books': books})
