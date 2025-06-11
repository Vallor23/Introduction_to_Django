# Update Operation

This command updates the title of a specific book instance.

## Python Command

```python
from bookshelf.models import Book

book = Book.objects.get(id=1)
book.title = "The Great Gatsby (First Edition)"
book.save()
```

## Output

No output, but the title is updated in the database.