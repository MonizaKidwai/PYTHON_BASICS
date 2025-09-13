# Check string is Pallindrome or not.
a = "MALAYALAM"

b = ""
for i in range(len(a)-1,-1,-1):
    b =b + a[i]

if b ==a:
    print("Your string is Pallindrome")
else:
    print("Its not a Pallindrome.")

