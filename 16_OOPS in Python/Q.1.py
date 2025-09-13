# Create a class Car with attributes brand and price. Add a method show_details() that prints the car info. Create an object and call the method.
# OOPs example

class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_details(self):
        print("Brand:", self.brand)
        print("Price:", self.price)

# Creating object
my_car = Car("Toyota", 800000)
my_car.show_details()



