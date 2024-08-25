import random

def roll_dice():
    while True:
        input("Press Enter to roll the dice...")
        roll = random.randint(1, 6)
        print(f"You rolled a {roll}!")
        again = input("Roll again? (yes/no): ").lower()
        if again != "yes":
            break

roll_dice()
