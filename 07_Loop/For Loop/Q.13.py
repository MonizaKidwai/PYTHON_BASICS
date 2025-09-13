# Count all letters, digits, and special symbols from a given string.

a = "ksydiugb@#$&^*hjsd12563"

char = 0
digit = 0
spchr = 0

for i in a:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        char+= 1
    else:
        spchr += 1
print(f"Your Digits are {digit}\nYour Alphabets are {char}\nYour Special Characters are {spchr} ")