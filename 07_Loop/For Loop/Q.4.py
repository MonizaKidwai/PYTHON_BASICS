# Take a number as input and print its table
n = int(input("Which Table you want: "))

for i in range(1,11):
    print(f"{n} * {i} = {n * i}")