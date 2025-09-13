Name = input("Please tell your Name: ")
Age = int(input("Tell your Age: "))

if Age >= 18:
    print(f"Hello {Name} You are a Valid Voter.")

else:
    years_left = 18 - Age
    print(f"Hello {Name}, You are not a Valid Voter.")
    print(f"You can vote after {years_left} year(s).")
