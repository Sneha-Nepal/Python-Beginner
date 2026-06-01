import random
import word_bank as wb

# Uniquness: Filtering the word_list i.e allowing user to choose the category for the word
while True:

    choose_category = int(input("Which category do you want the word from? Science = 1, world = 2, people = 3, programming = 4, random = 5\n"))

    if choose_category == 1:
        word_list =  wb.science
        break
    elif choose_category == 2:
        word_list = wb.world
        break
    elif choose_category == 3:
        word_list = wb.people
        break
    elif choose_category == 4:
        word_list = wb.programming
        break
    elif choose_category == 5:
        word_list = wb.random_list
        break
    else:
        print("Choose from 1 - 5 only.")


word = random.choice(word_list)
word_as_list = list(word)
# print(" ".join(word_as_list)) # For reference

# The game core programming concept is from here
placeholder = []

for space in range(len(word)):
    placeholder.append("_")
    
print(" ".join(placeholder))

lives = 3
game_over = False

while not game_over:
    
    user_guess = input("Make a guess: ").lower()
    
    if user_guess in placeholder:
        print("Already Guessed it")
        continue

    for index in range(len(word)):
        if user_guess == word[index]:
            placeholder[index] = user_guess 
        else:
            continue

    if user_guess not in word:
        lives -= 1
        print("Letter not in the word.")
        if lives == 0:
            print("You lose")
            print(f"The word was {word}")
            break

    print(f"Lives Left: {lives}")

    print(" ".join(placeholder))
    print()
    
    if "_" not in placeholder:
        print("You win")
        game_over = True