# Retrieve a Book Entry

To retrieve a book from the database using Django's ORM, use the `get` method:

```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
