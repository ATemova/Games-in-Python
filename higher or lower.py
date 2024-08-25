import random

def higher_or_lower():
    number_to_guess = random.randint(1, 100)
    guess = random.randint(1, 100)
    attempts_left = 10

    print("Try to guess the number between 1 and 100.")

    while attempts_left > 0:
        print(f"Your guess: {guess}")
        if guess < number_to_guess:
            print("Higher!")
        elif guess > number_to_guess:
            print("Lower!")
        else:
            print("Congratulations! You've guessed the number.")
            break

        guess = int(input("Enter a new guess: "))
        attempts_left -= 1
        print(f"Attempts left: {attempts_left}")

    if attempts_left == 0:
        print(f"Game over! The number was {number_to_guess}.")

higher_or_lower()
