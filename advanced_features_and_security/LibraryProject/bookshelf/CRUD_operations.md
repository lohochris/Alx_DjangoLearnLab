# CRUD Operations for Book Model

## 1. Create a Book
```python
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)  # Output: 1984 by George Orwell (1949)


book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

book.title = "Nineteen Eighty-Four"
book.save()
print(Book.objects.get(id=book.id))  # Output: Nineteen Eighty-Four by George Orwell (1949)

book.delete()
print(Book.objects.all())  # Output: <QuerySet []>
