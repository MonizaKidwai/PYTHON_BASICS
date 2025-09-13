# Create a class Point with x and y. Override __str__ to print coordinates nicely.

# Dunder method example

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

# Object usage
p = Point(4, 7)
print(p)