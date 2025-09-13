# Create a decorator that logs when a function is called. Apply it to a function say_hello().

# Decorator example

def log(func):
    def wrapper():
        print("Function is being called...")
        func()
    return wrapper

@log
def say_hello():
    print("Hello, Moniza!")

say_hello()