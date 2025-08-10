import random

while True:
    inp = str(input("Roll a dice? (y/n) :").lower())
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if inp == "y":
        print(f"You rolled {dice1} and {dice2}")
    elif inp == "n":
        print("Thanks for playing")
        break
    else:
        print("Invaild roll")
