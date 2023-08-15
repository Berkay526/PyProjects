import random

choices_list = ["rock", "paper", "scissors"]

user: str = input("enter 'rock' for rock, 'scissors' for scissors and 'paper' for paper: ")
bot = random.choice(choices_list)

if user != "rock" and user != "paper" and user != "scissors":
    print('enter "rock", "paper" or "scissors"')
else:
    player_status: list = [user, bot]
    if player_status  == ["rock", "paper"] or player_status  == ["paper", "scissors"] or player_status  == ["scissors", "rock"]:
        print("bot won")
    elif player_status == ["paper", "rock"] or player_status  == ["scissors", "paper"] or player_status  == ["rock", "scissors"]:
        print("user won")
    else:
        print("draw")