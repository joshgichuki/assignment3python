

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print(f"Reading '{self.title}' by {self.author}.")

    def info(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")

# Inheritance example
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size  # in MB

    def info(self):
        super().info()
        print(f"File Size: {self.file_size}MB")

# Example usage
book1 = Book("1984", "George Orwell", 328)
ebook1 = EBook("Digital Fortress", "Dan Brown", 356, 2)

book1.read()
book1.info()
ebook1.read()
ebook1.info()

print("\n--- Polymorphism Challenge ---")

# Activity 2: Polymorphism Challenge

class Vehicle:
    def move(self):
        print("Vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()