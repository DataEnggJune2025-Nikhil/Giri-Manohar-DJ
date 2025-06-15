import random
import os
import sys
from hangman_art import stages  # Contains Hangman ASCII art stages

# Maximum incorrect attempts (7) 
MAX_ATTEMPTS = len(stages)

# Clear terminal screen when game starts
os.system('cls' if os.name == 'nt' else 'clear')

def load_words(filename="words.txt"):
    """
    Reads words from file that are 5 and 6 characters long.
    Args:
        filename (str): Name of file that load words. Default is "words.txt".
    Returns:
        list: A list of valid lowercase words.
    Error Raises:
        SystemExit: If the file doesn't exist or is empty, the program exits.
    """
    try:
        with open(filename, 'r') as file:
            words = [line.strip().lower() for line in file if 5 <= len(line.strip()) <= 6]
        if not words:
            raise ValueError("!!!! Word list is empty or no words meet the length requirement !!!!")
        return words
    except FileNotFoundError:
        print(f"!!!! Error: The file '{filename}' was not found !!!!")
        sys.exit()
    except Exception as e:
        print(f" Unexpected error while loading words: {e}")
        sys.exit()


def choose_random_word(word_list):
    """
    Picks one random word from the list.

    Args:
        word_list (list): A list of technical words.

    Returns:
        str: A randomly selected word.
    """
    return random.choice(word_list)


def display_hangman(wrong_count):
    """
    Shows the current hangman stage based on wrong guesses player made.

    Args:
        wrong_count (int): Current number of wrong guesses.

    """
    print(stages[wrong_count])


def display_game_state(word, guessed_letters, wrong_letters, wrong_count):
    """
    Prints the game progress:
    - Which letters in the word have been guessed
    - Letters guessed incorrectly
    - How many attempts are left
    - Current hangman stage

    Args:
        word (str): The actual word.
        guessed_letters (set): Correctly Guessed letters.
        wrong_letters (list): Incorrectly Guessed letters.
        wrong_count (int): Count of incorrect guesses.
    """
    display = [letter if letter in guessed_letters else '_' for letter in word]
    print("Word: " + ' '.join(display).upper())
    print("Wrong letters: " + ' '.join(wrong_letters).upper())
    # print("Guessed letters: " + ' '.join(sorted(guessed_letters | set(wrong_letters))).upper())
    print(f"Attempts remaining: {MAX_ATTEMPTS - wrong_count}")
    display_hangman(wrong_count)


def get_player_guess(guessed_letters):
    """
    Asks the player to input a letter.
    Exception handling & Input is validated to ensure it is new, single alphabetical character.
    Allows the user to exit by typing 'exit'.

    Args:
        guessed_letters (set): Set of guessed letters.

    Returns:
        str: A new valid letter.
    Exits:
        If user types 'exit' word
    """
    while True:
        try:
            guess = input("\nEnter a letter (or type 'exit' to quit): ").strip().lower()
            if guess == 'exit':
                print("Exiting the game. Goodbye!")
                sys.exit()
            elif not guess:
                print("!!!! Input cannot be empty !!!!")
            elif len(guess) != 1:
                print("!!!! Only Enter a single letter !!!!")
            elif not guess.isalpha():
                print("!!!! Please enter only alphabet letters !!!!")
            elif guess in guessed_letters:
                print("!!!! You've already guessed that letter !!!!")
            else:
                return guess
        except KeyboardInterrupt:
            print("\n !!!! Game interrupted. Goodbye !!!!")
            sys.exit()
        except Exception as e:
            print(f"!!!! Unexpected error: {e} !!!!")


def check_game_over(word, guessed_letters, wrong_count):
    """
    Checks if the player has either won or lost the game.
    Prints a message in either case.
    Returns True if the game should end, otherwise False.

    Args:
        word (str): The actual word
        guessed_letters (set): Correctly guessed letters.
        wrong_count (int): Count of wrong guesses so far.

    Returns:
        bool: True if Game is over, if not False.
    """
    if all(letter in guessed_letters for letter in word):
        print("╔══════════════════════════════════════════╗")
        print(f"  Congratulations! The word is: {word.upper()}   ")
        print("╚══════════════════════════════════════════╝")
        return True
    elif wrong_count >= MAX_ATTEMPTS:
        print("╔═════════════════════════════════════════╗")
        print(f"  Game Over! The word was: {word.upper()}   ")
        print("╚═════════════════════════════════════════╝")
        return True
    return False


def play_hangman():
    """
    Runs the entire game loop:
    - Loads the word
    - Handles player input
    - Updates the game state
    - Ends when the player wins or loses
    - Gives a hint after 4 wrong guesses
    - Asks if the player wants to play again
    """
    try:
        word_list = load_words()
        word = choose_random_word(word_list)
        guessed_letters = set()
        wrong_letters = []
        wrong_count = 0

        while True:
            display_game_state(word, guessed_letters, wrong_letters, wrong_count)
            guess = get_player_guess(guessed_letters | set(wrong_letters))

            if guess in word:
                guessed_letters.add(guess)
                print("\nGood guess!\n")
            else:
                wrong_letters.append(guess)
                wrong_count += 1
                print("\nWrong guess!\n")

                # Sgow a letter after 4 incorrect guesses
                if wrong_count == 4:
                    unrevealed = [ch for ch in word if ch not in guessed_letters]
                    if unrevealed:
                        hint = random.choice(unrevealed)
                        guessed_letters.add(hint)
                        print(f"Hint: The letter '{hint.upper()}' has been revealed!\n")

            if check_game_over(word, guessed_letters, wrong_count):
                break

        # Ask user if they want to play game again
        again = input("\n Want to play again? (y/n): ").strip().lower()
        if again == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            play_hangman()
        else:
            print("\nThanks for Playing :)\n")
    except Exception as e:
                # Catch-all for anything unexpected
        print(f"\n !!!! Unexpected error in game loop: {e} !!!!")
        sys.exit()


def main():
    """
    Main program entry point.
    Prints the title and starts the game.
    """
    print("\n=== HANGMAN GAME === \n")
    play_hangman()


if __name__ == "__main__":
    main()
