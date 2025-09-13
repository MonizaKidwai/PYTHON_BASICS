# Create a class BankAccount with a private balance. Add methods to deposit and show balance. Prevent direct access to balance.

# Encapsulation example

class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("Balance:", self.__balance)

# Object usage
acc = BankAccount()
acc.deposit(1000)
acc.show_balance()