import random

shot = 6
difficulty = input("Select a difficulty (easy(between 1 and 50 both of are included), med(between 1 and 100 both of are included), hard(between 1 and 150 both of are included)): ")

# this assignment is neccessary otherwise "num" will become an unbound variable in the while loop
num: int = 0

match difficulty:
    case "easy":
        num = random.randint(1, 50)
    case "med":
        num = random.randint(1, 100)
    case "hard":
        num = random.randint(1, 150)
    case _:
        print("Enter a valid level.")

try:
    while shot > 0:
        guess = int(input("Enter an integer number: "))
        if guess < num:
            shot -= 1
            print(f"Try a bigger value, {shot} shots left.")
        elif guess > num:
            shot -= 1
            print(f"Try a smaller value, {shot} shots left.")
        else:
            print('You won!')
            break
    else:
        print("You lost!")
except TypeError:
    print("Enter an integer value")