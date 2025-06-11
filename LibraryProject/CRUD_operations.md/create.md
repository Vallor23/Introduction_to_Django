# 📘 Create Book

This operation creates a new `Book` entry in the database using the Django shell.

## 💻 Command

```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
... author="George Owell"
... publication_year="1984-06-09",
)

print(book)
```

## Output

1984
