# Create a random number guessing game with python.
import random
num = random.randint(1,10)
tries = 0

while True:
    guess = int(input("Please guess your number between 1 and 10: "))


    if num == guess:
        tries += 1
        print(f"You are right you guessed the number is {tries} tries.")
        break
    
    elif num < guess:
        print("Go a little lower")
        tries += 1
    elif num > guess:
        print("Go a little Higher")
        tries += 1
    else:
        tries += 1
        print("Sorry you are wrong")

