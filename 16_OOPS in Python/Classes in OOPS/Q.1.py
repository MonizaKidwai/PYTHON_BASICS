# Create a class Book with attributes title and author. Add a method details() that prints both. Create one object and call the method.

# Class example

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def details(self):
        print("Title:", self.title)
        print("Author:", self.author)

# Object creation
b1 = Book("Python Basics", "Moniza")
b1.details()