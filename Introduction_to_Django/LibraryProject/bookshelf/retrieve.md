## Retrieving a Book Instance

```python
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()

# Display all books
for book in books:
    print(book)
#Expected Output: <Book: 1984 by George Orwell>