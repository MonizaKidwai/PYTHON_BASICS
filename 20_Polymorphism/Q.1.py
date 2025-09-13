# Create two classes Cat and Dog, both with a method speak(). Call the method using a loop to show polymorphism.

# Polymorphism example

class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Woof")

# Using polymorphism
animals = [Cat(), Dog()]
for animal in animals:
    animal.speak()