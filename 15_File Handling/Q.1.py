# Write a program that creates a file named info.txt, writes your name and age into it, then reads and prints the content.

# File handling example

# Writing to file
with open("info.txt", "w") as f:
    f.write("Name: Moniza\n")
    f.write("Age: 22\n")

# Reading from file
with open("info.txt", "r") as f:
    content = f.read()
    print("File Content:\n", content)



