# Write a program that asks for a number and divides 100 by it. Handle the case where the user enters zero or invalid input.
# Exception handling example
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")



