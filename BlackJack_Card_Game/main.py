import random

# there is no 1. For ace is only 11
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print("Welcome to BlackJack Card Game!")
start= input("Would you like to start?'y' or 'n': ")

# to store the cards of user(initials and the ones being added)
# comp_cards = [] 
# user_cards = []

total_players = {
    'comp_cards' : [],
}

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
        print(f"Player{player_num} Card: {player_cards}")


def add_cards(player_cards):
    # add cards of user and dealer

    another_card = random.choice(cards)
    player_cards.append(another_card)

    if player_cards == total_players['comp_cards']:
        print(f"Dealer Card: {total_players['comp_cards']}")
    else:
        print(f"Dealer Card: {total_players['comp_cards'][0]} & hidden")

    print(f"Your Card: {user_cards}")

def calculator(lst):
    # helper function to calculate sum
    return sum(lst)


def final_score(total_user, total_comp):
    # to calculate the final score and decide result

    print(f"Your Total: {total_user}")
    print(f"Dealer Total: {total_comp}")
    
    if total_user > 21:
        print("You Lose!")
    elif total_comp > 21:
        print("You Win!")
    elif total_user > total_comp:
        print("You Win!")
    elif total_comp == total_user:
        print("Draw!")
    else:
        print("You Lose!")
    


if start == 'y':
    number_of_players = int(input("Enter the number of players: "))
    for i in range(number_of_players):
        total_players[f"player{i+1}"] = []

    #Stating two cards i.e. game start
    deal_initial_cards(number_of_players)

    go_again = True
    while go_again:
        next_move = input("'hit' or 'stand': ")

        # add cards to the user
        if next_move == 'hit':
            add_cards(user_cards)
            total_user = calculator(user_cards)
            if total_user > 21:
                print("You went over 21!")
                go_again =False

        # dealer add cards 
        elif next_move == 'stand':
            while sum(total_players['comp_cards']) < 17:
                add_cards(total_players['comp_cards'])
                total_comp = calculator(total_players['comp_cards'])

            go_again = False

        else:
            print("Type 'y' or 'n' only!")

        #Calculate the total and declare winner
        if go_again == False:
            final_score(total_user, total_comp)  

else:
    print("See you soon!")

print("Game Over!")
