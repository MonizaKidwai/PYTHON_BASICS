#  Accept a number and print its reverse
a = int(input("Tell your Number: "))
rev = 0
while a > 0:
    rev = rev * 10 + a % 10
    a = a // 10
print(rev)