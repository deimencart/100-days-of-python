import random
from hangman_words import word_list       # Import list of possible words
from hangman_art import stages, logo      # Import hangman art stages and game logo


# TODO-1: Use the 'word_list' from hangman_words.py
print(logo)                               # TODO-3: Print the logo at the start of the game
lives = 6                                 # Number of lives (incorrect guesses allowed)

# Randomly select a word for the player to guess
chosen_word = random.choice(word_list)
# print(chosen_word)                      # Debug Only: Uncomment to see the answer

# Create an initial placeholder string with underscores
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

# Game state trackers
game_over = False
correct_letters = []                      # Stores correct guessed letters
guessed_letter = []                       # Stores all guessed letters (correct + wrong)

# Main game loop
while not game_over:

    # TODO-6: Show how many lives remain
    print(f"**************************** {lives}/6 LIVES LEFT ****************************")
    
    # Ask for a guess
    guess = input("Guess a letter: ").lower()
    
    # TODO-4: If the letter was already guessed, notify and skip the rest of the loop
    if guess in guessed_letter:
        print(f"You have already guessed: {guess}")
        print(stages[lives])               # Show current hangman stage
        continue
    guessed_letter.append(guess)           # Add new guess to guessed list

    # Build the display string for the current turn
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter               # Correct guess: reveal the letter
        elif letter in correct_letters:
            display += letter               # Previously guessed correctly: keep revealed
        else:
            display += "_"                  # Not yet guessed: keep hidden

    # Show updated word state
    print(f"Word to guess: {display}")

    # Add correct guess to the correct_letters list if not already there
    if guess in chosen_word and guess not in correct_letters:
        correct_letters.append(guess)

    # TODO-5: If wrong guess, lose a life and show message
    if guess not in chosen_word:
        lives -= 1
        print(f"Letter '{guess}' is not part of the word, you lose a life")

        # If no lives left, game over (loss)
        if lives == 0:
            game_over = True
            # TODO-7: Show correct word when losing
            print("*********************** YOU LOSE **********************")
            print(f"The correct word was: {chosen_word}")

    # Check for win (no underscores left in display)
    if "_" not in display:
        game_over = True
        print("**************************** YOU WIN ****************************")

    # TODO-2: Use the stages list from hangman_art.py to draw hangman
    print(stages[lives])
