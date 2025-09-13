# Create a base class Person with attributes name and age. Create a derived class Student that adds grade. Print all details using inheritance.

# Inheritance example

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

# Object creation
s1 = Student("Aisha", 20, "A+")
print("Name:", s1.name)
print("Age:", s1.age)
print("Grade:", s1.grade)