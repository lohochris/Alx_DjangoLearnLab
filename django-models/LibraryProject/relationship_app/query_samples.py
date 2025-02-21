from relationship_app.models import Author, Book, Library, Librarian

# Create Authors
author1 = Author.objects.create(name="George Orwell")
author2 = Author.objects.create(name="J.K. Rowling")

# Create Books
book1 = Book.objects.create(title="1984", author=author1)
book2 = Book.objects.create(title="Animal Farm", author=author1)
book3 = Book.objects.create(title="Harry Potter", author=author2)

# Create Libraries
library1 = Library.objects.create(name="Central Library")
library2 = Library.objects.create(name="Community Library")

# Add Books to the Libraries
library1.books.set([book1, book2])
library2.books.set([book3])

# Create Librarians
librarian1 = Librarian.objects.create(name="John Doe", library=library1)
librarian2 = Librarian.objects.create(name="Jane Smith", library=library2)

# Sample Queries
print("Books by George Orwell:")
books_by_orwell = Book.objects.filter(author__name="George Orwell")
for book in books_by_orwell:
    print(book.title)

print("\nBooks in Central Library:")
books_in_central = library1.books.all()
for book in books_in_central:
    print(book.title)

print("\nLibrarian for Central Library:")
print(library1.librarian.name)

# New Function to Get Library by Name
def get_library_by_name(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library
    except Library.DoesNotExist:
        return None

# Testing the new query
print("\nTesting get_library_by_name() function:")
test_library = get_library_by_name("Central Library")
if test_library:
    print(f"Library Found: {test_library.name}")
else:
    print("Library not found.")
