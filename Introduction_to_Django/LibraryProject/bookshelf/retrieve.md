# Retrieve a Book Entry

To retrieve a book from the database using Django's ORM, use the `get` method:

### **Retrieve a Book by ID**
```python
from bookshelf.models import Book

book = Book.objects.get(id=1)  # Retrieves the book with ID 1
print(book.title, book.author, book.publication_year)
