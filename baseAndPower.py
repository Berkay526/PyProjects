enter: str = input("enter 'enter' or 'e' if you want to enter numbers, enter 'no' or 'n' if you don\'t: ")
base: int = 0
power: int = 0
number: int = 0
view_inputs: str = ""

while enter == "enter" or enter == "e":
    base: int = int(input('''enter an integer that you want to use as a base number: '''))
    power: int = int(input('''enter an integer that you want to use as power of the base: '''))
    number = base ** power
    print(f"base: {base}, power: {power} and number: {number}")

    the_last_numbers: tuple = (base, power, number)

    view_inputs = input('enter "show" to view your latest inputs and the result: ')
    
    if view_inputs == "show":
        [print(items) for items in the_last_numbers]
    else:
        continue

    enter: str = input("enter 'enter' or 'e' if you want to enter numbers, enter 'no' or 'n' if you don\'t: ")
else:
    print("quitting.")               