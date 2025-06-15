# Hangman Game

This is a Python Console Project **Hangman Game**. The code demonstrates file I/O, control flow, input validation, error handling, docstring, and ASCII art.

---

## How to Run the Program

1. Make sure Python 3 is installed on system.
2. Clone or Download this repository.
3. Ensure the following files exist in the project directory:
    - `hangman.py` (main script)
    - `hangman_art.py` (ASCII visuals)
    - `words.txt` (50 words with 5–6 letters long)
4. Open a terminal in the project folder and run:

```bash
python hangman.py
````

---

## Features Implemented

* Random word selection from a list (`words.txt`)
* Game interface shows:

  * Word having underscore for Hidden letters
  * Incorrect Letters user guessed
  * Remaining attempts
  * ASCII hangman drawing that updates with user guess
* Input validation:

  * Accepts only single alphabet characters
  * Not consider repeated character
  * Allows `exit` command to quit anytimes
  
* Detects win/loss and ends game appropriately
* Replay prompt after game ends
* Detailed inline documentation and error handling
* Automatically clears the screen when game starts or restart

---

## Bonus Features Added

* ✅ **Hint System**: If the player makes 4 wrong guesses, one letter is automatically revealed.
* ✅ **Exit**: Player can type `exit` or use `Ctrl+C` to quit anytime.

---

## Known Limitations or bugs

* Words must be present in `words.txt` with 5 or 6 letters.
* Does not support multiplayer or custom word entry yet.

---

## Sample Gameplay

```

=== HANGMAN GAME === 

Word: _ _ _ _ _ _
Wrong letters: 
Attempts remaining: 7

      +---+
          |
          |
          |
         ===
    

Enter a letter (or type 'exit' to quit): a

Wrong guess!

Word: _ _ _ _ _ _
Wrong letters: A
Attempts remaining: 6

      +---+
      O   |
          |
          |
         ===
    

Enter a letter (or type 'exit' to quit): e

Good guess!

Word: _ _ _ _ E _
Wrong letters: A
Attempts remaining: 6

      +---+
      O   |
          |
          |
         ===
    

Enter a letter (or type 'exit' to quit): i

Good guess!

Word: _ _ I _ E _
Wrong letters: A
Attempts remaining: 6

      +---+
      O   |
          |
          |
         ===

Enter a letter (or type 'exit' to quit): 
```
#### ... game continues until win or loss (Refer Screenshots)
---

## Project Main Structure

```
hangman_project/
├── hangman.py          # Main game file
├── words.txt          # Word list file
├── README.md          # Project documentation
└── hangman_art.py     # ASCII art
```

---

## Credits

* Giri Manohar Vemula (Game Developer)
* Nikhil Sharma (Game Designer)

---

