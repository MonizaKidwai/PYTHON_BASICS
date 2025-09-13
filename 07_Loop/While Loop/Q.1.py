#  Separate each digit of a number and print it on the new line.
a = int(input("Tell your Number: "))

while a > 0:
    print(a % 10)
    a = a // 10