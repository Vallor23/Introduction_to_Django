# 📙 Retrieve Books

This operation retrieves all `Book` records from the database.

## 💻 Command

```python
from bookshelf.models import Book

books = Book.objects.all()
for book in books:
    print(book.id, book.title, book.author, book.publication_year)
```

## Output

1 The Great Gatsby F. Scott Fitzgerald 1925-04-10
3 1984 George Orwell 1949-06-08

## You can also retrieve a specific book using its ID:

```python
book = Book.objects.get(id=1)
print(book.title)
```

## output: The Great Gatsby