import random
from game_data import data

print("Ready to Find the Most Popular Person?")

def most_popular(first_person, second_person):
    if first_person > second_person:
        return first_person
    elif second_person > first_person:
        return second_person
    else:
        return 0
    

def game_on(popular_person):
    user_choice = input(f"Does {person1['name']} have more followers than {person2['name']}? Yes or No: ").lower()

    if user_choice == "yes":
        if person1['follower_count'] == popular_person:
            return "correct"
    elif user_choice == "no":
        if person1['follower_count'] != popular_person:
            return "correct"
    else:
        return "ERROR"

person1 = random.choice(data)
person2 = random.choice(data)
# For testing
print(person1)
print(person2)

popular_person = most_popular(person1['follower_count'], person2['follower_count'])
# For testing
print(popular_person)

# Game logic
again = True
while again:
    result = game_on(popular_person)
    if result != "correct":
        again = False

print("Game Over!")
