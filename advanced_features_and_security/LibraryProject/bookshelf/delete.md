
---

### **`delete.md`**  
```md
## Deleting a Book Instance

```python
from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Verify deletion by retrieving all books again
books = Book.objects.all()
print(books) #Expected Output:<QuerySet []>
