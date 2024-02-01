import random

a = ["Rock", "Paper", "Scissors"]
b = random.choice(a)
n = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors."))

if a[n] == b:
    print(f"Your move : {a[n]}")
    print(f"Opponent's move : {b}")
    print("DRAW")
elif a[n] != b:
    if a[n] == "Rock" and b == "Scissors":
        print(f"Your move : {a[n]}")
        print(f"Opponent's move : {b}")
        print("YOU WIN")
    elif a[n] == "Paper" and b == "Rock":
        print(f"Your move : {a[n]}")
        print(f"Opponent's move : {b}")
        print("YOU WIN")
    elif a[n] == "Scissors" and b == "Paper":
        print(f"Your move : {a[n]}")
        print(f"Opponent's move : {b}")
        print("YOU WIN")
    elif a[n] == "Rock" and b == "Paper":
        print(f"Your move : {a[n]}")
        print(f"Opponent's move : {b}")
        print("YOU LOSE")
    elif a[n] == "Paper" and b == "Scissors":
        print(f"Your move : {a[n]}")
        print(f"Opponent's move : {b}")
        print("YOU LOSE")
    elif a[n] == "Scissors" and b == "Rock":
        print(f"Your move : {a[n]}")
        print(f"Opponent's move : {b}")
        print("YOU LOSE")