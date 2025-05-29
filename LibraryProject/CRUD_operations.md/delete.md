# Delete Operation

This command deletes a specific book from the database.

## Python Command

```python
from bookshelf.models import Book

book = Book.objects.get(id=1)
book.delete()
```

## Output

(1, {'bookshelf.Book': 1})