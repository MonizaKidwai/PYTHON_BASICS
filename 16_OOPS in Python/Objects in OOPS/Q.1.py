# Create a class Laptop with attributes brand and price. Create two objects and print their details.

# Objects example

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

# Creating objects
l1 = Laptop("HP", 55000)
l2 = Laptop("Dell", 62000)

print("Laptop 1:", l1.brand, "-", l1.price)
print("Laptop 2:", l2.brand, "-", l2.price)