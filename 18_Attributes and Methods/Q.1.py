# Create a class Circle with attribute radius. Add a method area() that returns the area of the circle.

# Attributes and methods example

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Object and method call
c1 = Circle(5)
print("Area of circle:", c1.area())