# Magic methods = Dunder methods (double underscore) __init__, __Str__, __eq__
# They are automatically called by many of pythons built-in operations.
# They allow developers to define or customize the behaviour of objects

class Book:

    # constructor
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, item):
        return item in self.title or item in self.author

    def __getitem__(self, item):
        if item == 'title':
            return self.title
        elif item == 'author':
            return self.author
        elif item == 'num_pages':
            return self.num_pages
        else:
            return f"Key {item} was not found"


book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 297)
book3 = Book("The Lion, the witch and the Wardrobe", "C.S. Lewis", 197)
book4 = Book("The Hobbit", "J.R.R. Tolkien", 310)
print(book1)
print(book1 == book4)
print(book1 > book2)
print(book1 < book3)
print(book1 + book3)
print("Lion" in book3)
print(book1['title'])