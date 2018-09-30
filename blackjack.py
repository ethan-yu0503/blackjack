import os
import random

# Defining the suits and ranks of a given card
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
ranks = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

player_hands = []
player_bids = []
player_chips = []


def create_deck():
    # Create a full deck with 52 cards
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((suit, rank))
    return deck


def deal(hand, deck):
    # Place one card from the deck to a hand
    hand.append(deck.pop())


def calc_score(hand):
    # Calculate the score of a given hand
    total = 0
    at_least_one_ace = False
    for card in hand:
        if card[1] == "Jack" or card[1] == "Queen" or card[1] == "King":
            total += 10
        elif card[1] == "Ace":
            total += 1
            at_least_one_ace = True
        else:
            total += card[1]
    if at_least_one_ace is True and total <= 11:
        total += 10
    return total


def card_details(card):
    # Return information about a specific card
    return str(card[1]) + " of " + card[0]


def hand_details(player_hand):
    # Return card information and score of a given hand
    hand_str = "You have "
    for card in player_hand:
        hand_str += card_details(card) + ", "
    hand_str += "for a total of " + str(calc_score(player_hand))
    return hand_str


def dealer_details(dealer_hand):
    # Return information about the dealer. Starts differently from player.
    hand_str = "The dealer has "
    for card in dealer_hand:
        hand_str += card_details(card) + ", "
    hand_str += "for a total of " + str(calc_score(dealer_hand))
    return hand_str


def player_is_bust(player_hand):
    # To find out if a player busted!
    if calc_score(player_hand) > 21:
        return True
    else:
        return False 


def blackjack(hand):
    # To find out if a player got blackjack!
    if calc_score(hand) == 21:
        return True
    else:
        return False


def clear():
    # Commands for clearing the terminal when necessary
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')


def reveal_results(dealer_hand, player_hands, player_chips, player_bids):
    # Redistribute chips based on everyone's cards and amount bid

    # Evaluating results for every single player
    for i in range(len(player_hands)):
        if player_is_bust(player_hands[i]):
            print("Player " + str(i + 1) + " busted, losing " + str(player_bids[i]) + " chips.")
            player_chips[i] -= player_bids[i]

        elif blackjack(player_hands[i]) is True and blackjack(dealer_hand) is False:
            print("Player " + str(i + 1) + " got blackjack, winning " + str(player_bids[i] * 2) + " chips.")
            player_chips[i] += player_bids[i] * 2

        elif not player_is_bust(dealer_hand) and calc_score(player_hands[i]) > calc_score(dealer_hand):
            print("Player " + str(i + 1) + " wins, winning " + str(player_bids[i]) + " chips!")
            player_chips[i] += player_bids[i]
        
        elif player_is_bust(dealer_hand):
            print("The dealer busted. Player " + str(i + 1) + " wins " + str(player_bids[i]) + " chips!")
            player_chips[i] += player_bids[i]
    
        elif calc_score(player_hands[i]) < calc_score(dealer_hand):
            print("Player " + str(i + 1) + " lost, losing " + str(player_bids[i]) + " chips!")
            player_chips[i] -= player_bids[i]
        
        elif calc_score(player_hands[i]) == calc_score(dealer_hand):
            print("Player " + str(i + 1) + " had a draw! No chips were lost!")


def display_players_stats(num_players):
    # Print out information about each player when a round ends or someone quits
    for i in range(num_players):
        print("Player " + str(i + 1) + " has " + str(player_chips[i]) + " chips.")


def restart_game():
    # Clearing the player cards and bids to prepare for the next game
    del player_hands[:]
    del player_bids[:]


def player_bankrupts(players):
    # Determining if any player has 0 chips remaining
    for chip_remaining in players:
        if chip_remaining == 0:
            return True
    return False


def game():
    clear()
    enter_game = False
    while enter_game is False:
        # Catching invalid input for number of players
        try:
            num_players = int(input("Welcome to BlackJack!\nHow many players are playing? (Up to 3)"))
            if num_players > 3 or num_players < 1:
                print("That is an invalid number of players. Try again!")
            else:
                enter_game = True
        except ValueError:
            print("Please type an integer between 0 and 3")

    print("The game is starting! Each player gets 500 chips to start out with!")
    for i in range(num_players):
        player_chips.append(500)

    while not player_bankrupts(player_chips):
        global_deck = create_deck()
        random.shuffle(global_deck)

        dealer_hand = []
        deal(dealer_hand, global_deck)
        deal(dealer_hand, global_deck)

        print("The dealer is showing a " + card_details(dealer_hand[0]))
        for i in range(num_players):
            print("Player " + str(i + 1) + ": it's your turn!")
            player_hand = []
            valid_bid = False
            while valid_bid is False:
                # Catching invalid input for amount to bid
                try:
                    bid = int(input("How much would you like to bid? You have " + str(player_chips[i]) + " chips."))
                    if bid < 0 or bid > player_chips[i]:
                        print("That is an invalid amount to bid. Try again!")
                    else:
                        valid_bid = True
                        player_bids.append(bid)
                except ValueError as e:
                    print("Please type a valid integer for bidding!")
            
            deal(player_hand, global_deck)
            deal(player_hand, global_deck)

            print(hand_details(player_hand))

            while player_is_bust(player_hand) is False:
                choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
                clear()
                if choice == "h":
                    deal(player_hand, global_deck)
                    print(hand_details(player_hand))
                    if player_is_bust(player_hand) is True:
                        print("Player " + str(i + 1) + " busted!")
                        player_hands.append(player_hand)
                        break

                elif choice == "s":
                    print("Player " + str(i + 1) + ", your total is: " + str(calc_score(player_hand)))
                    player_hands.append(player_hand)
                    break

                elif choice == "q":
                    print("Ending game...")
                    display_players_stats(num_players)
                    exit()
                else:
                    print("Invalid choice. Try again.")

        # Dealer's Turn
        while calc_score(dealer_hand) < 17:
            deal(dealer_hand, global_deck)

        print(dealer_details(dealer_hand))
        if player_is_bust(dealer_hand):
            print("The dealer busted!")

        reveal_results(dealer_hand, player_hands, player_chips, player_bids)
        display_players_stats(num_players)
        restart_game()
        if player_bankrupts(player_chips) is False:
            print("\nNew round coming up!\n")

    print("Someone lost all of their chips! Therefore, the dealer wins! Thanks for playing!")


if __name__ == "__main__":
    game()