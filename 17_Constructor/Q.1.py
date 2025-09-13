# Create a class User with a constructor that takes username and email. Print both using the constructor.

# Constructor example

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

# Creating object
u1 = User("moniza22", "moniza@example.com")
print("Username:", u1.username)
print("Email:", u1.email)