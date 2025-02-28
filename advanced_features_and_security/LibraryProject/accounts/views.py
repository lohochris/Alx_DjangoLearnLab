from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView
from .models import Book
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

class PublishBookView(PermissionRequiredMixin, ListView):
    model = Book
    template_name = 'bookshelf/book_list.html'
    permission_required = 'bookshelf.can_publish_books'
    raise_exception = True  # This will raise a 403 error if permission is denied


@permission_required('bookshelf.can_publish_books', raise_exception=True)
def publish_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
