import random

game = ["r", "p", "s"]
chances = 5
trials = 0
cp = 0
up = 0

print("r for Rock \t p for Paper \t s for Scissor")

while trials < chances:

    op = input("\nEnter your choice: ")
    comp = random.choice(game)
    print(f"Computer chose {comp}")

    if op == 'r':
        if comp == 'r':
            print("Tied, no point to anyone!")
            print(f"Now You have {up} and Computer has {cp} points")
            trials = trials + 1

        elif comp == 'p':
            print("Computer got 1 point")
            cp += 1
            print(f"Now You have {up} and Computer has {cp} points")
            trials = trials + 1

        elif comp == 's':
            print("You got 1 point")
            up += 1
            print(f"Now You have {up} and Computer has {cp} points")
            trials = trials + 1


    elif op == 'p':
        if comp == 'p':
            print("Tied, no point to anyone!")
            print(f"Now You have {up} and Computer has {cp} points")
            trials = trials + 1

        elif comp == 's':
            print("Computer got 1 point")
            cp += 1
            print(f"Now You have {up} and Computer has {cp} points")
            trials = trials + 1

        elif comp == 'r':
            print("You got 1 point")
            up += 1
            print(f"Now You have {up} and Computer has {cp} points")
            trials = trials + 1


    elif op == 's':
        if comp == 's':
            print("Tied, no point to anyone!")
            print(f"Now You have {up} and Computer has {cp} points")
            trials = trials + 1

        elif comp == 'r':
            print("Computer got 1 point")
            cp += 1
            print(f"Now You have {up} and Computer has {cp} points")
            trials = trials + 1

        elif comp == 'p':
            print("You got 1 point")
            up += 1
            print(f"Now You have {up} and Computer has {cp} points")
            trials = trials + 1

        else:
            print("Invalid input !")
            trials = trials + 1

    print(f"{chances - trials} chances left")

print("\nGAME OVER")

if up == cp:
    print("\nGame Tied")

elif up > cp:
    print("\nHurray, You won the game !")

else:
    print("\nOopps, You lost, Computer won !")



