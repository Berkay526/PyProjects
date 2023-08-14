import random

choices_list = ["rock", "paper", "scissors"]

user: str = input("enter 'rock' for rock, 'scissors' for scissors and 'paper' for paper: ")
bot = random.choice(choices_list)

while user == "rock" or user == "paper" or user == "scissors":
    match user, bot:
        case "rock", "paper":
            print("bot won")
            break
        case "paper", "scissors":
            print("bot won")
            break
        case "scissors", "rock":
            print("bot won")
            break
        case "rock", "scissors":
            print("user won")
            break
        case "paper", "rock":
            print("user won")
            break
        case "scissors", "paper":
            print("user won")
            break
        case _:
            print("draw")
            break
else:
    print('enter "rock", "paper" or "scissors"')