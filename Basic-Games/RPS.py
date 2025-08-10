import random

choices = ["r", "p", "s"]
emojis = {"r": "🪨", "p": "📃", "s": "✂️"}

while True:
    userChoice = input("Rock, paper or Scissors ? (r/p/s) :")
    computerChoice = random.choice(choices)

    if userChoice == computerChoice:
        print("It's a tie!")
        print(f"You chose {emojis[userChoice]}")
        print(f"Computer chose {emojis[computerChoice]}")
    elif (
        (userChoice == "r" and computerChoice == "s")
        or (userChoice == "p" and computerChoice == "r")
        or (userChoice == "s" and computerChoice == "p")
    ):
        print(f"You chose {emojis[userChoice]}")
        print(f"Computer chose {emojis[computerChoice]}")
        print("You won!")
    else:
        print(f"You chose {emojis[userChoice]}")
        print(f"Computer chose {emojis[computerChoice]}")
        print("You lose!")

    con = input("Continue ? (y/n):")
    if con == "n":
        break
