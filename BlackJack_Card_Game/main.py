import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print("Welcome to BlackJack Card Game!")
start= input("Would you like to start?'y' or 'n': ")

comp_cards = [] 
user_cards = []

def deal_initial_cards():

    for _ in range(2):
        comp1 = random.choice(cards)
        user1 = random.choice(cards)
        comp_cards.append(comp1)
        user_cards.append(user1)

    print(f"Dealer Card: {comp_cards[0]} and Hidden")
    print(f"Your Card: {user_cards}")
    #For testing easier
    print(f"Test_comp_cards: {comp_cards}")


def add_cards(player_cards):
    another_card = random.choice(cards)
    player_cards.append(another_card)

    print(f"Dealer Card: {comp_cards[0]} & hidden")
    print(f"Your Card: {user_cards}")

def calculator(lst):
    return sum(lst)


def final_score(total_user, total_comp):
    print(f"Your Total: {total_user}")
    print(f"Dealer Total: {total_comp}")
    
    if total_user > 21:
        print("You Lose!")
    elif total_comp > 21:
        print("You Win!")
    elif total_user > total_comp:
        print("You Win!")
    else:
        print("You Lose!")
    


if start == 'y':
    deal_initial_cards()

    go_again = True
    while go_again:
        next_move = input("'hit' or 'stand': ")

        if next_move == 'hit':
            add_cards(user_cards)
            total_user = calculator(user_cards)
            total_comp = calculator(comp_cards)  
            if total_user > 21:
                print("You went over 21!")
                final_score(total_user, total_comp)
                go_again =False

        elif next_move == 'stand':
            final_score(total_user, total_comp)

            go_again = False
            break

        else:
            print("Type 'y' or 'n' only!")

else:
    print("See you soon!")

print("Game Over!")
