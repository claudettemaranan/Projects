import os


def get_player1_number():
    while True:
        try:
            secret_number = int(input("\nPlayer 1, enter a secret number between 1 to 10: "))
            
            if 1 <= secret_number <= 10:
                return secret_number
            else:
                print("\nPlease enter a number between 1 and 10.")
        except:
            print("\nInvalid input. Please enter a number.")


def get_player2_guess():
    while True:
        try: 
            player2_guess = int(input("\nPlayer 2, guess the secret number: "))
 
            if 1 <= player2_guess <= 10:
                return player2_guess
            else: 
                print("\nPlease enter a number between 1 and 10.")
        except:
            print("\nInvalid input. Please enter a number.")


def main():
    while True: 
        print("\nWelcome to the Number Guessing Game!")
        
        secret_number = get_player1_number()
        os.system("cls" if os.name == "nt" else "clear")
        
        max_attempt = 7 
        guess_count = 0
        guessed_numbers = []
            
        while guess_count < max_attempt:
            player2_guess = get_player2_guess()

            if player2_guess in guessed_numbers:
                print("\nYou have already entered that number! Try again.")
                continue
            
            guess_count += 1
            guessed_numbers.append(player2_guess)

            if player2_guess == secret_number:
                print(f"\nCongratulations, Player 2! You guessed the number {secret_number} in {guess_count} tries.")
                break
            elif player2_guess > secret_number:
                print(f"\nLower! Attempts left: {max_attempt - guess_count}")
            else:
                print(f"\nHigher! Attempts left: {max_attempt - guess_count}")
        
        if guess_count == max_attempt:
            print(f"\nSorry, Player 2. You ran out of attempts. The secret number was {secret_number}.")

        retry = input("\nPlay again? (yes/no): ")
        
        if retry.strip().lower() != 'yes':
            print("\nThank you for playing!")
            break

main()
