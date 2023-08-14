import random

choices_list = ["rock", "paper", "scissors"]

user: str = input("enter 'rock' for rock, 'scissors' for scissors and 'paper' for paper: ")
bot = random.choice(choices_list)

match user, bot:
    case "rock", "paper":
        print("bot won")
    case "paper", "scissors":
        print("bot won")
    case "scissors", "rock":
        print("bot won")
    case "rock", "scissors":
        print("user won")
    case "paper", "rock":
        print("user won")
    case "scissors", "paper":
        print("user won")
    case _:
        print("draw")