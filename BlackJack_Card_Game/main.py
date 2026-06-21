import random

# there is no 1. For ace is only 11
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print("Welcome to BlackJack Card Game!")
start= input("Would you like to start?'y' or 'n': ")


total_players = {
    'comp_cards' : [],
}

total_sum_cards = []

def deal_initial_cards(number_of_players):
    # stating two cards of dealer and users, but dealer second card is hidden.

    for _ in range(2):
        comp_initals = random.choice(cards)
        total_players['comp_cards'].append(comp_initals)
        for num in range(number_of_players):
            user_initals = random.choice(cards)
            total_players[f"player{num+1}"].append(user_initals) 
        

    print(f"Dealer Card: {total_players['comp_cards'][0]} and Hidden")
    #For testing easier
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

            next_move = input(f"'hit' or 'stand' for player{num + 1}: ")

            # add cards to the user
            if next_move == 'hit':
                updated_cards = add_cards(total_players[f"player{num + 1}"])
                print(updated_cards)

            # dealer add cards 
            elif next_move == 'stand':
                player_cards = total_players[f"player{num + 1}"]
                print(f"Final Cards for player{num + 1}: {player_cards}")
                total_sum_cards.append(calculator(player_cards))
                break

            else:
                print("Type 'hit' or 'stand' only!")


            # Check if over 21
            total_sum = calculator(updated_cards)
            if total_sum > 21:
                print(f"Your cards are {updated_cards}. You went over 21!")
                break


    #Calculate the total and declare winner
    

else:
    print("See you soon!")

print("Game Over!")
