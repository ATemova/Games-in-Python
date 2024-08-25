import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 5
    print("Welcome to the Number Guessing Game!")
    print("You have 5 attempts to guess the correct number between 1 and 100.")
    
    for attempt in range(attempts):
        guess = int(input(f"Attempt {attempt + 1}: Enter your guess: "))
        
        if guess == number_to_guess:
            print("Congratulations! You guessed the correct number.")
            return
        elif guess < number_to_guess:
            print("Too low!")
        else:
            print("Too high!")
    
    print(f"Sorry, you're out of attempts. The correct number was {number_to_guess}.")

# Run the game
number_guessing_game()
