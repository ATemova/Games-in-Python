def guess_the_word():
    words = ["python", "programming", "developer", "computer"]
    word_to_guess = random.choice(words)
    guessed_word = "_" * len(word_to_guess)
    attempts_left = 5

    print("Guess the word!")
    
    while attempts_left > 0 and "_" in guessed_word:
        print("Current word:", " ".join(guessed_word))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in word_to_guess:
            guessed_word = "".join([guess if word_to_guess[i] == guess else guessed_word[i] for i in range(len(word_to_guess))])
        else:
            attempts_left -= 1
            print(f"Wrong guess. Attempts left: {attempts_left}")

    if "_" not in guessed_word:
        print(f"Congratulations! You've guessed the word: {word_to_guess}")
    else:
        print(f"Game over! The word was: {word_to_guess}")

guess_the_word()
