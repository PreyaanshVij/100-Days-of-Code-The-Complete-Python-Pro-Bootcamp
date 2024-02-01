print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

a = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'.")

if a == "left":
    print("A rock fell on you from a cliff and you died.")
    print("GAME OVER")
else :
    b = input("There is an island in the middle of the lake. Type 'wait' to wait for a boat. "
              "Type 'swim' to swim across.")
    if b == "swim" :
        print("You were eaten by the crocodiles in the lake.")
        print("GAME OVER")
    else :
        print("You arrive at the island unharmed.")
        c = input("There is a house with 3 doors. One red, one yellow "
                  "and one blue. Which color do you choose?")
        if c == "red":
            print("You were burnt to crisp.")
            print("GAME OVER")
        elif c == "blue":
            print("You were drowned in a chamber filled with water.")
            print("GAME OVER")
        else :
            print("You reached the treasure and became rich.")
            print("Congratulations!!!")