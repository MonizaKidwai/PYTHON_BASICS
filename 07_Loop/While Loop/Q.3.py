#  Accept a number and check if it is a pallindromic number (If number and its reverse are equal)
a = int(input("Tell your Number: "))
copy = a
rev = 0

while a > 0:
    rev = rev * 10 + a % 10
    a = a // 10

if copy == rev:
    print("Pallindromic number.")
else:
    print("Not a Pallindromic number.")