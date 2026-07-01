import random

print("Welcome to HIgher_Lower Game!")
print()

# Defining global variable
chance = 10

def game_on(chance):
    required_number = random.randint(1,100)

    while chance != 0:
        guess = int(input("Guess the number: "))

        if guess == required_number:
            print(f"Correct! The number was {guess}.")
            break

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


again = 'yes'
while again == 'yes':
    game_on(chance)
    again = input("do you want to play again? 'yes' or 'no': ").lower()

print("See you again!")
