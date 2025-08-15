# Hangman Game – Python Implementation

## 📌 Overview
This is a Python console implementation of the classic **Hangman** game.  
The player must guess the hidden word letter-by-letter within a limited number of lives.  
For each wrong guess, a part of the hangman drawing appears until the player runs out of lives.

---

## 🎯 Features
- **Random Word Selection**: Pulls words from `hangman_words.py`.
- **ASCII Art Stages**: Visual representation of the hangman from `hangman_art.py`.
- **Input Validation**: Checks for repeated guesses and notifies the player.
- **Win/Loss Conditions**: Displays appropriate end-game messages.
- **Lives Tracking**: Starts with 6 lives and decreases with each wrong guess.

---

## 🗂 Project Structure
```text
📂 hangman_project/
├── hangman.py # Main game file
├── hangman_words.py # Contains the list of possible words
├── hangman_art.py # Contains hangman ASCII art stages & logo
└── README.md # Project documentation

```

### File-by-file

- **hangman.py**  
  Runs the game: prints logo, picks a random word, handles guesses, lives, and shows `stages`.

- **hangman_words.py**  
  Exposes a list named `word_list` used by `hangman.py`.

- **hangman_art.py**  
  Exposes:
  - `logo`: string printed at game start
  - `stages`: list of 7 ASCII frames (index 6 → 0) matching lives

---

## 📄 Minimal File Stubs

> Paste these into their respective files to get a working baseline.

### `hangman_words.py`
```python
# List of lowercase words for the game
word_list = [
    "python", "variable", "function", "loop", "module",
    "object", "class", "string", "integer", "boolean"
]
```
## ⚙ Requirements
- Python **3.x**
- No external libraries required


## 🖥 How to Run
1. **Clone** or download the repository.
2. Open a terminal in the project folder.
3. Run:
   ```bash
   python hangman.py

## 📜 How It Works
1. **Import Dependencies**
   - `random` for selecting a random word
   - `word_list` from `hangman_words.py`
   - `stages` & `logo` from `hangman_art.py`

2. **Game Initialization**
   - Display the game logo
   - Select a random word from the word list
   - Create a placeholder with underscores for each letter

3. **Game Loop**
   - Show lives remaining
   - Ask the user for a letter guess
   - If the letter was already guessed, notify the user and skip
   - Update the display with correct guesses
   - If the guess is wrong, decrease lives and show a message
   - Check for win/loss conditions
   - Display the hangman ASCII stage for the current number of lives

4. **End Game**
   - **Win:** All letters guessed before running out of lives
   - **Lose:** Lives reach zero; reveal the correct word


🖼 Example Gameplay

**************************** 6/6 LIVES LEFT ****************************
Word to guess: _ _ _ _ _
Guess a letter: a
Letter 'a' is not in the word. You lose a life.
 +---+
 |   |
 O   |
     |
     |
     |
=========

📌 Notes

    You can uncomment the print(chosen_word) line for debugging.

    The game assumes that stages contains 7 ASCII art stages (index 6 → 0).

    Words in hangman_words.py should be lowercase for consistent comparison.

