import random

def hangman():
    word_list = ['python', 'javascript', 'java', 'kotlin', 'swift']
    word_to_guess = random.choice(word_list).lower()
    guessed_word = ['_'] * len(word_to_guess)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print(" ".join(guessed_word))

    while attempts > 0 and "_" in guessed_word:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        print(" ".join(guessed_word))

    if "_" not in guessed_word:
        print("Congratulations! You guessed the word.")
    else:
        print(f"Game Over! The word was '{word_to_guess}'.")

# Run the game
hangman()
