# Use the abc module to create an abstract class Shape with a method area(). Create a subclass Rectangle that implements it.

# Abstraction example

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Object usage
r = Rectangle(5, 3)
print("Area:", r.area())