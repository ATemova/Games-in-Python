import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts_left = 10

    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while attempts_left > 0:
        guess = int(input("Enter your guess: "))
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You've guessed the number.")
            break
        attempts_left -= 1
        print(f"Attempts left: {attempts_left}")

    if attempts_left == 0:
        print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")

number_guessing_game()
