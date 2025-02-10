## Creating a Book Instance

```python
from bookshelf.models import Book

# Creating a new book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Display the created book
print(book)
 

# Output: 1984 by George Orwell (1949)
