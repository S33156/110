import random

def roll_dice():
    return random.randint(1, 6)

def print_dice(number):
    if number == 1:
        print(" --------- ")
        print("|         |")
        print("|    0    |")
        print("|         |")
        print(" --------- ")
    elif number == 2:
        print(" --------- ")
        print("|   0     |")
        print("|         |")
        print("|     0   |")
        print(" --------- ")
    elif number == 3:
        print(" --------- ")
        print("|   0     |")
        print("|    0    |")
        print("|     0   |")
        print(" --------- ")
    elif number == 4:
        print(" --------- ")
        print("| 0   0   |")
        print("|         |")
        print("| 0   0   |")
        print(" --------- ")
    elif number == 5:
        print(" --------- ")
        print("| 0   0   |")
        print("|    0    |")
        print("| 0   0   |")
        print(" --------- ")
    elif number == 6:
        print(" --------- ")
        print("| 0   0   |")
        print("| 0   0   |")
        print("| 0   0   |")
        print(" --------- ")

def main():
    response = "y"
    
    while response == "y":
        roll = roll_dice()
        print_dice(roll)
        response = input("Do you want to roll again? (y/n): ").lower()
        
    print("Goodbye!")

if __name__ == "__main__":
    main()
