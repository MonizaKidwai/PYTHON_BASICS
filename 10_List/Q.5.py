# Check if List is sorted or not.

a = [12,13,18,15,16]

for i in range(len(a)- 1):
    if a[i] < a[i+1]:
        continue
    else:
        print("Your list is not Sorted")
        break
else:
    print("Your list is sorted")