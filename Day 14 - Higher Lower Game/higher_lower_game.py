import random
from art import logo, vs
from game_data import data


def game(first_random_person, score):
    # Print the higher lower game logo art
    print(logo)

    # Display A person from the random choosen
    print(f"Compare A: {first_random_person['name']}, a {first_random_person['description']}, from {first_random_person['country']}.")

    second_random_person = random.sample(list(data), 1)[0]
    while first_random_person['name'] == second_random_person['name']:            
        second_random_person = random.sample(list(data), 1)[0]

    # Print the higher lower game vs art
    print(vs)

    # Display B person from the random choosen
    print(f"Against B: {second_random_person['name']}, a {second_random_person['description']}, from {second_random_person['country']}.")        

    winner = 'B'
    if first_random_person['follower_count'] > second_random_person['follower_count']:
        winner = 'A'

    prediction = input("Who has more followers? Type 'A' or 'B': ")

    if prediction == winner:
        score += 1
        print(f"You're right! Current score: {score}.")
        first_random_person = second_random_person
        return game(first_random_person, score)
    return score


# Select a random person from the list of personalities
first_random_person = random.sample(list(data), 1)[0]

game_score = 0
score = game(first_random_person, game_score)

print("\n" * 20)    
print(f"Sorry, that's wrong. Final score: {score}")

