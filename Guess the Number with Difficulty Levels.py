import random

def guess_the_number_with_difficulty():
    print("Choose difficulty level: 1 (Easy), 2 (Medium), 3 (Hard)")
    level = int(input("Enter level: "))

    if level == 1:
        upper_bound = 10
        attempts = 5
    elif level == 2:
        upper_bound = 50
        attempts = 7
    elif level == 3:
        upper_bound = 100
        attempts = 10
    else:
        print("Invalid level.")
        return

    number_to_guess = random.randint(1, upper_bound)

    print(f"Guess the number between 1 and {upper_bound}")

    while attempts > 0:
        guess = int(input("Enter your guess: "))
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You've guessed the number.")
            break
        attempts -= 1
        print(f"Attempts left: {attempts}")

    if attempts == 0:
        print(f"Sorry, the number was {number_to_guess}.")

guess_the_number_with_difficulty()
