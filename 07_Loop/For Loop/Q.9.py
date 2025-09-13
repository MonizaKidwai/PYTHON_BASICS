# Accept a number and check if it a perfect number or not.

n = int(input("Check your number is perfect or not: "))
sum = 0
for i in range(1,n):
    if n%i == 0:
        sum = sum + i

if sum == n:
    print("Your number is Perfect")
else:
    print("Not a perfect number.")
