import random

us = 0
cs = 0
ties = 0
again = "y"

while again == "y":
    u = input("Choose R, P, or S: ").upper()
    if u != "R" and u != "P" and u != "S":
        print("That's not a valid choice, try again")
    else:
        c = random.choice("RPS")
        print("Computer picked", c)
        if u == c:
            print("Tie!")
            ties += 1
        elif u == "R" and c == "S":
            print("Rock breaks scissors, you win!")
            us += 1
        elif u == "P" and c == "R":
            print("Paper covers rock, you win!")
            us += 1
        elif u == "S" and c == "P":
            print("Scissors cut paper, you win!")
            us += 1
        else:
            print("Computer wins this one")
            cs += 1
        print("Score: You", us, "- Computer", cs, "- Ties", ties)
    again = input("Play again? (y/n): ").lower()
print(us, cs, ties)