import os 

hammer = """





                        -=[ gavel ]=-  2/01



                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                   jgs/_______________\



"""



bid_dictionary = {}




def add_bidder(name, bid):
    bid_dictionary[name] = bid

def get_highest_bidder(dictionary):
    highest_bid = 0
    winner = ""
    for name, bid in dictionary.items():
        if bid > highest_bid:
            highest_bid = bid
            winner = name
    return winner, highest_bid


def main(): 
    print("Welcome to the secret auction program.")
    while True:
        name = input("What is your name?: ")
        bid = int(input("What is your bid?: $"))
        add_bidder(name, bid)
        more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        if more_bidders.lower() != "yes":

# Source - https://stackoverflow.com/a/2084628
# Posted by poke, modified by community. See post 'Timeline' for change history
# Retrieved 2026-08-05, License - CC BY-SA 3.0
            os.system('cls || clear')
            break

    winner, highest_bid = get_highest_bidder(bid_dictionary)
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

if __name__ == "__main__":
    print(hammer)
    main()
    