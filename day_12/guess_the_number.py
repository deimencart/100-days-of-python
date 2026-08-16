import os 
import random
from _guess_the_number_banner import print_the_banner



def main(): 
    while True: 
        print("Welcome to the Guess the Number Game!")
        print("I'm thinking of a number between 1 and 100.")
        print ("Choose a difficulty level: ")
        print ("1. Easy (10 attempts)")
        print ("2. Hard (5 attempts)")
        
        difficulty = input("Enter your choice (1/2): ").strip().lower()
        
        if difficulty == "easy":
            attempts = 10
        elif difficulty == "hard":
            attempts = 5
        else:
            print("Invalid choice. Defaulting to Hard difficulty.")
            attempts = 5
        
        number_to_guess = random.randint(1, 100)
        
        while attempts > 0:
            try:
                guess = int(input(f"You have {attempts} attempts left. Enter your guess: "))
            except ValueError:
                print("Please enter a valid integer.")
                continue
            
            if guess < 1 or guess > 100:
                print("Your guess must be between 1 and 100.")
                continue
            
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} correctly!")
                break
            
            attempts -= 1
        
        if attempts == 0:
            print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console for better readability
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break


if __name__ == "__main__":
    print_the_banner()
    main()