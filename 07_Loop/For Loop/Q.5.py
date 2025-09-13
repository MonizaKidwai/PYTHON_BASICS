# Sum up to n terms
n = int(input("Tell your Number: "))

sum = 0

for i in range(1,n+1):
    sum = sum + i

print(f"Your Sum is {sum}")