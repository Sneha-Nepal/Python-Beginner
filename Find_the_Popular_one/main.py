import random
from game_data import data

print("Ready to Find the Most Popular Person?")

def initial_person():
    person1 = random.choice(data)
    return person1


def most_popular(first_person, second_person):
    if first_person['follower_count'] > second_person['follower_count']:
        return first_person
    elif second_person['follower_count'] > first_person['follower_count']:
        return second_person
    else:
        return 0
    

def game_on(popular_person):
    user_choice = input(f"Does {person1['name']} have more followers than {person2['name']}? Yes or No: ").lower()

    if user_choice == "yes":
        if person1 == popular_person:
            return "correct"
    elif user_choice == "no":
        if person1 != popular_person:
            return "correct"
    else:
        return "incorrect"


# Game logic
count = 0
again = True
person1 = initial_person()
while again:

    # person1 = random.choice(data)
    person2 = random.choice(data)
    # For testing
    print(person1)
    print(person2)

    # Person1 and person2 to not be same
    while person1 == person2:
        person2 = random.choice(data)

    popular_person = most_popular(person1, person2)
    # For testing
    print(popular_person)


    result = game_on(popular_person)
    if result != "correct":
        again = False
    elif result == 'correct':
        count += 1
    else:
        print("ERROR")

    
    # Keep track of the score
    print(f"Your score is {count}.")

    # To keep comparing with the same person until more popular one is found
    person1 = popular_person


print("Game Over!")

