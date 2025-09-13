T = int(input("Tell the Temperature: "))
if T < 0:
    print("Freezing Cold")
elif T >= 0 and T < 10:
    print("Very Cold")
elif T >= 10 and T < 20:
    print("Cold")
elif T >= 20 and T < 30:
    print("Pleasant")
elif T >= 30 and T < 40:
    print("Hot")

else:
    print("Very Hot")
