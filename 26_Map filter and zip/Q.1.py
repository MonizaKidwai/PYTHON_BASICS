# Use map to square numbers, filter to keep even numbers, and zip to pair names with scores.

# Map, Filter, Zip example

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
names = ["Aisha", "Rahul", "Zoya"]
scores = [88, 92, 85]
paired = list(zip(names, scores))

print("Squared:", squared)
print("Even numbers:", evens)
print("Paired:", paired)