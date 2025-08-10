import random

low = 1
high = 100
guess = random.randint(low, high)

guesses = 0
while True:
    num = int(input("Enter a number between 1 and 100: "))
    guesses += 1
    if num == guess:
        print("Bullseye")
        print(f"Guesses took: {guesses}")
        break
    elif num > guess:
        print("Too high")
    else:
        print("Too low")
