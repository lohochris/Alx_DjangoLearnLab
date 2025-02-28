# bookshelf/views.py

# Import necessary modules
from django.shortcuts import render
from django.db.models import Q
from .models import Book
from .forms import BookSearchForm

def search_books(request):
    # Initialize the form and the books list
    form = BookSearchForm(request.GET or None)
    books = []

    # Check if the form is valid and perform the search
    if form.is_valid():
        query = form.cleaned_data['query']
        # Use Django ORM with icontains for case-insensitive matching
        books = Book.objects.filter(title__icontains=query)
    
    # Render the template with the form and search results
    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})
