import random
import time

number: int = random.randint(1, 7)
retry: str = input('enter "r" or "roll" if you wanna roll the dice, otherwise enter "quit": ')

while retry == "r" or retry == "roll":
    print("dice is getting rolled...")
    time.sleep(1)
    print(f"number of our dice: {number}")
    time.sleep(1)
    retry: str = input('enter "r" or "roll" if you wanna roll the dice, otherwise enter "quit": ')
print("bye...")