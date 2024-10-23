"""Number guessing game."""

from art import logo
import random


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

number = random.choice(range(1, 100))

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard':  ").lower()
attempts_count = EASY_LEVEL_ATTEMPTS if difficulty_level == "easy" else HARD_LEVEL_ATTEMPTS
print(f"You have {attempts_count} attempts remaining to guess the number.")


def continue_guessing(guess_number):
    """Guess until you have attempts."""
    if guess_number < number:
        print("Too low.")
    elif guess_number > number:
        print("Too high.")

    print(f"You have {attempts_count} attempts remaining to guess the number.")


while attempts_count > 0:
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The answer was {number}")
        attempts_count = 0
    else:
        continue_guessing(guess)
        attempts_count -= 1
        if attempts_count == 0:
            print("You've run out of guesses, you lose.")

