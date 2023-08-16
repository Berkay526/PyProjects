import random

choices_list = ["rock", "paper", "scissors"]

user: str = input("enter 'rock' for rock, 'scissors' for scissors and 'paper' for paper: ")
bot = random.choice(choices_list)

player_status: list = [user, bot]

try:
    match player_status:
        case ["rock", "paper"] | ["paper", "scissors"] | ["scissors", "rock"]:
            print(f"bot won \nuser: {user} \nbot: {bot}")
        case ["paper", "rock"] | ["scissors", "paper"] | ["rock", "scissors"]:
            print(f"user won \nuser: {user} \nbot: {bot}")
        case _:
            print(f"draw \nuser: {user} \nbot: {bot}")
except ValueError:
    print('enter "rock", "paper" or "scissors"')
