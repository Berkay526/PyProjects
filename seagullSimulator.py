import random

class Fish():
    def __init__(self, location_x_in_sea = random.randrange(1, 4), location_y_in_sea = random.randrange(1, 4), energy = 50, nutrition = 1) -> None:
        self.energy = energy
        self.location_x_in_sea = location_x_in_sea
        self.location_y_in_sea = location_y_in_sea
        self.nutrition = nutrition

seagull_energy: int = 300
seagull_hunger = 1
Fish()

print('''Welcome to seagull simulator!
         You will try to catch a fish!
         You have a 3*3 field as a sea.
         If you can catch the fish without burning all of your energy, you will win!
         But if you can\'t, you\'ll lose!
         Let\'s start''')

print("." * 50)

catch = input('Enter "catch" or "c" to try to catch a fish, you can quit the game using "q": ')

while catch != "q":
    if (catch == "catch" or catch == "c"):
        hunting_point_x_in_sea: int = int(input("Enter the x position of point of the sea that you wanna dive (you can enter 1, 2 or 3): "))
        hunting_point_y_in_sea: int = int(input("Enter the y position of point of the sea that you wanna dive (you can enter 1, 2 or 3): "))
    
        hunting_point: tuple = (hunting_point_x_in_sea, hunting_point_y_in_sea)
        fish_location = (Fish().location_x_in_sea, Fish().location_y_in_sea)

        match hunting_point:
            case (1, 1) | (1, 2) | (1, 3) | (2, 1) | (2, 2) | (2, 3) | (3, 1) | (3, 2) | (3, 3):
                if hunting_point == fish_location:
                    seagull_energy += Fish().energy
                    seagull_hunger -= Fish().nutrition
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
            case _:
                print("Enter a valid integer.")
    else:
        print("Enter a valid command.")
        catch = input('Enter "catch" or "c" to try to catch a fish, you can quit the game using "q": ')
else:
    print("See you.")