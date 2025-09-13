Year = int(input("Enter Your Year: "))


if Year %100 == 0 and Year % 400 == 0:
    print("Its a Leap Year")
elif Year %100 != 0 and Year %4 == 0: 
    print("Its a Leap Year")

else:
    print("Its a Normal Year")
