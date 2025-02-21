
---

### **`update.md`**  
```md
## Updating a Book Instance

```python
from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"

# Save changes
book.save()

# Display updated book
print(book)
#Expected Output:<Book: Nineteen Eighty-Four by George Orwell>