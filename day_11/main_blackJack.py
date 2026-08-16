from _black_jack_banner import print_black_banner
import random
import os


deck  = ["11", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"]


def calculate_score(cards):
    score = sum(int(c) for c in cards)
    aces = cards.count("11")
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    return score

def blackjack_game():
    user_cards = []
    casino_cards = []
    for _ in range(2):
        user_cards.append(random.choice(deck))
    print (f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
    casino_cards.append(random.choice(deck))
    print(f"Casino's first card: {casino_cards[0]}")
    usr_input = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    while usr_input == "y":
        user_cards.append(random.choice(deck))
        print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
        if calculate_score(user_cards) > 21:
            print("You went over. You lose 😭")
            return
        usr_input = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    while calculate_score(casino_cards) < 17:
        casino_cards.append(random.choice(deck))
    print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
    print(f"Casino's final hand: {casino_cards}, final score: {calculate_score(casino_cards)}")
    if calculate_score(casino_cards) > 21:
        print("Casino went over. You win 😁")
    elif calculate_score(user_cards) > calculate_score(casino_cards):
        print("You win 😁" )
    elif calculate_score(user_cards) < calculate_score(casino_cards):
        print("You lose 😭")
    else:
        print("It's a draw 🙃")
    


def main():
    print("Welcome to the Blackjack Game!")
    while True: 
        user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if user_input == "y":
            os.system('cls || clear')
            blackjack_game()
        elif user_input == "n":
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid input. Please type 'y' or 'n'.")

    



if __name__ == "__main__":
    print_black_banner()
    main()



