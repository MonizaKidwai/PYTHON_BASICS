# Write a function that accepts any number of positional and keyword arguments. Print them separately.

# Args and Kwargs example

def show_details(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# Function call
show_details("Math", "Science", name="Aisha", age=20)