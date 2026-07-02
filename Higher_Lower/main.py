import random

print("Welcome to HIgher_Lower Game!")
print()

def game_on(chance, required_number):
    while chance != 0:
        guess = int(input("Guess the number: "))

        if guess == required_number:
            print(f"Correct! The number was {guess}.")
            print()
            return 'Win'

        elif guess < required_number:
            print("Too Low")
            chance -= 1
            print(f"You have {chance} chance left.")

        elif guess > required_number:
            print("Too High")
            chance -= 1
            print(f"You have {chance} chance left.")

        else:
            print("ERROR")
            break
    
    # If no chane remains
    if chance == 0:
        print("Game Over!")
        return 'Lose'



again = 'yes'
while again == 'yes':

    # Variable declaration for each new start
    level = 1
    required_number = 0
    chance = -1
    level_up = True

    # Loop for leveling up
    while level_up:
        if level == 1:
            required_number = random.randint(1,50)
            chance = 10
        elif level == 2:
            required_number = random.randint(1,100)
            chance = 8
        elif level == 3:
            required_number = random.randint(1,250)
            chance = 5
        else:
            print("You have completed all the levels!")
            break

        print(f"Level: {level}")
        print(f"{required_number}")             # For testing 
        result = game_on(chance, required_number)

        # Leveling up or ending the game
        if result == 'Win':
            level +=1
        elif result == 'Lose':
            level_up = False
            break
        else:
            print("ERROR")

    # Asking the user if they want to play again from the start
    again = input("do you want to play again? 'yes' or 'no': ").lower()
    print()

print("See you again!")
