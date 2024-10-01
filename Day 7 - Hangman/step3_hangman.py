import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

guesses = []
game_over = False

while not game_over:
    display = ""
    guess = input("Guess a letter: ").lower()
    guesses.append(guess)

    for letter in chosen_word:
        if letter in guesses:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You Win")