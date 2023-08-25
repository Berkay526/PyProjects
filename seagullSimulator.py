import random

class Fish():
    def __init__(self, location_x_in_sea = random.randrange(1, 5), location_y_in_sea = random.randrange(1, 5), energy = 50, nutrition = 1) -> None:
        self.energy = energy
        self.location_x_in_sea = location_x_in_sea
        self.location_y_in_sea = location_y_in_sea
        self.nutrition = nutrition

seagull_energy: int = 500
seagull_hunger = 3
fish = Fish()
[fish for _ in range(1, 15)]

print('''Welcome to seagull simulator!
         You will try to catch fishes!
         If you can catch 3 fishes without burning all of your energy, you will win!
         But if you can\'t, you\'ll lose!
         Let\'s start''')

print("." * 50)

catch = input('Enter "catch" or "c" to try to catch a fish, you can quit the game using "q": ')

while (catch == "catch" or catch == "c"):
    hunting_point_x_in_sea: int = int(input("Enter the x position of point of the sea that you wanna dive: "))
    hunting_point_y_in_sea: int = int(input("Enter the y position of point of the sea that you wanna dive: "))
    
    hunting_point: tuple = (hunting_point_x_in_sea, hunting_point_y_in_sea)
    fish_location = (fish.location_x_in_sea, fish.location_y_in_sea)

    if hunting_point == fish_location:
        seagull_energy += fish.energy
        seagull_hunger -= fish.nutrition
        print(f"You caught a fish! Now your energy: {seagull_energy} and hunger: {seagull_hunger}")

        if seagull_hunger == 0:
            print("You won!")
        else:
            catch = input('Enter "catch" or "c" to try to catch a fish, you can quit the game using "q": ')
    else:
        seagull_energy -= 50
        print(f"You missed it! Try again! Now your energy: {seagull_energy} and hunger: {seagull_hunger}")

        if seagull_energy == 0:
            print("You lost!")
        else:
            catch = input('Enter "catch" or "c" to try to catch a fish, you can quit the game using "q": ')
else:
    print("See you.")