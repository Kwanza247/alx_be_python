# File: oop/book_class.py

class Book:
    # Constructor - called when you create a new Book object
    def __init__(self, title, author, year):
        self.title = title        # Assign title to the object
        self.author = author      # Assign author to the object
        self.year = year          # Assign year to the object

    # Destructor - called when the object is deleted
    def __del__(self):
        print(f"Deleting {self.title}")

    # String representation (for humans)
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    # Official representation (for developers/debugging)
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
