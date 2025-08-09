# File: oop/library_system.py

# Base Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Derived Class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        # Call the constructor of the base class
        super().__init__(title, author)
        self.file_size = file_size  # in KB

# Derived Class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Call the constructor of the base class
        super().__init__(title, author)
        self.page_count = page_count

# Composition - Library class
class Library:
    def __init__(self):
        self.books = []  # Empty list to store book objects

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, "File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")