import random
import time

def number_memory_game():
    number = random.randint(1000, 9999)
    print("Memorize this number:", number)
    time.sleep(5)
    print("\033c", end="")  # Clear screen

    guess = int(input("Enter the number you memorized: "))

    if guess == number:
        print("Correct!")
    else:
        print(f"Wrong! The number was {number}.")

number_memory_game()
