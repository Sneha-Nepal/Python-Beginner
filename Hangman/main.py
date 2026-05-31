import random

word_list = ["cat", "dog", "python", "developer", "hangman", "quiz", "jazz", "fuzzy", "programming", "mystery"]

word = random.choice(word_list)
word_as_list = list(word)
# print(" ".join(word_as_list)) # For reference

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