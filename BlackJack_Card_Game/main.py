import random

# For ace is only 11. One(1) will be added in futhur update.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Initialization on top
total_players = {}

print("Welcome to BlackJack Card Game!")
start= input("Would you like to start?'y' or 'n': ")


def deal_initial_cards(number_of_players):
    # stating two cards of dealer and users, but dealer second card is hidden.

    for _ in range(2):
        comp_initals = random.choice(cards)
        total_players['comp_cards'].append(comp_initals)
        for num in range(number_of_players):
            user_initals = random.choice(cards)
            total_players[f"player{num+1}"].append(user_initals) 
        

    print(f"Dealer Card: {total_players['comp_cards'][0]} and Hidden")

    #For easier testing and debugging
    print(f"Test_comp_cards: {total_players['comp_cards']}")

    for player_num in range(number_of_players):
        player_cards = total_players[f"player{player_num + 1}"]
        print(f"Player{player_num + 1} Card: {player_cards}")


def add_cards(player_cards):
    # add cards of user and dealer

    another_card = random.choice(cards)
    player_cards.append(another_card)

    print("Card Added")
    return player_cards


def calculator(all_cards):
    # helper function to calculate sum
    return sum(all_cards)



if start == 'y':
    total_players['comp_cards'] = []

    number_of_players = int(input("Enter the number of players: "))

    # Create empty lists for all number of players
    for i in range(number_of_players):
        total_players[f"player{i+1}"] = []

    #Stating two cards in all empty lists
    deal_initial_cards(number_of_players)

    # Loop for one player at a time
    for num in range(number_of_players):

        # Go again for same player until stand or over for them
        go_again = True
        while go_again:

            next_move = input(f"'hit' or 'stand' for player{num + 1}: ").lower()

            # add cards to the user
            if next_move == 'hit':
                updated_cards = add_cards(total_players[f"player{num + 1}"])
                print(updated_cards)
                # Check if over 21
                total_sum = calculator(updated_cards)
                if total_sum > 21:
                    print(f"Your cards are {updated_cards}. You went over 21!")
                    go_again = False

            # dealer add cards 
            elif next_move == 'stand':
                player_cards = total_players[f"player{num + 1}"]
                print(f"Final Cards for player{num + 1}: {player_cards}")
                go_again = False

            else:
                print("Type 'hit' or 'stand' only!")

    # Dealer's turn after all players have played
    comp_total = calculator(total_players['comp_cards'])
    while comp_total < 17:
        dealer_updated_cards = add_cards(total_players['comp_cards'])
        comp_total = calculator(total_players['comp_cards'])


    #Calculate the total and declare winner
    comp_total = calculator(total_players['comp_cards'])
    for num in range(1, number_of_players + 1):
        player_lst = total_players[f"player{num}"]
        player_total = calculator(player_lst) 

        if player_total > 21:
            print(f"player{num} LOST (busted)")

        elif comp_total > 21:
            print(f"player{num} WINS (dealer busted)")

        elif player_total > comp_total:
            print(f"player{num} WINS ({player_total} > {comp_total})")

        elif player_total < comp_total:
            print(f"player{num} LOST ({player_total} < {comp_total})")

        else:  # player_total == dealer_total
            print(f"player{num} TIES with Dealer ({player_total} = {comp_total})")
        

else:
    print("See you soon!")

print("Game Over!")
