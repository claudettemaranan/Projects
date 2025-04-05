import os


def hangman():
    print("Welcome to Hangman!")

    
    # Player 1 enters a random word
    word = input("\nPlayer 1, enter a word: ").lower()
    os.system("cls")
    word_length = len(word)
    wrong_guesses = 0
    guessed_letters = []
    guessed_word = ['_'] * word_length


    # Loop until player 2 wins or loses
    while True:
        if wrong_guesses == 6:
            print(hangman_stages[wrong_guesses])
            # Player 2 loses
            print("\nGame over! Player 2 lost. The word was:", word)
            break

       
        # Print gallows and word progress
        print(hangman_stages[wrong_guesses])
        print("Word:", ' '.join(guessed_word))
        print("Tries left:", 6 - wrong_guesses)        
        print("Letters already guessed:"," ".join(guessed_letters))



        # Player 2 guesses a letter
        guess = input("Player 2, enter your guess: ").lower()


        # Check if player 2's guess is a single letter
        if len(guess) != 1:
            print("\nPlease enter a single letter.")
            continue
 

        # If the letter already exist
        if guess in guessed_letters:
            print("\nYou have already guessed that letter! Try again.")
            continue


        guessed_letters.append(guess)


        # If the letter is in the given word
        if guess in word:
            for i in range(word_length):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            wrong_guesses += 1
            print("\nWrong guess!")
            
            
        if '_' not in guessed_word:
            print(hangman_stages[wrong_guesses])
            print("\nCongratulations! Player 2 won. The word is:", word)
           
            break
        
    # New game
    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
       hangman()
    else:
        print("Thank you for playing Hangman!")


hangman_stages = [
        """
         +---+
         |   |
             |
             |
             |
             |
        =========
        |H E L P|
        """,
        """
         +---+
         |   |
         O   |
             |
             |
             |
        =========
        |H E L P|
        """,
        """
         +---+
         |   |
         O   |
         |   |
             |
             |
        =========
        |H E L P|
        """,
        """
         +---+
         |   |
         O   |
        /|   |
             |
             |
        =========
        |H E L P|
        """,
        """
         +---+
         |   |
         O   |
        /|\  |
             |
             |
        =========
        |H E L P|
        """,
        """
         +---+
         |   |
         O   |
        /|\  |
        /    |
             |
        =========
        |H E L P|
        """,
        """
         +---+
         |   |
         O   |
        /|\  |
        / \  |
             |
        =========
        |D E A D|
        """
    ]


hangman()
