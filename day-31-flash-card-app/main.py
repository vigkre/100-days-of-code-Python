"""Flash card project."""

from tkinter import Button, Canvas, PhotoImage, Tk

import pandas as pd
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
timer = None
current_card = {}

# ---------------------------- FUNCTIONS ------------------------------- #
# Read data from words to learn if not exists starts from scratch
try:
    words = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    words = pd.read_csv("./data/french_words.csv")
finally:
    to_learn = words.to_dict(orient="records")


def next_card():
    """
    Displays the next flashcard with a French word.

    This function cancels any existing timer for flipping the card,
    randomly selects a new word from the `to_learn` list, updates the
    canvas to show the French word on the front of the card, and sets
    a new timer to automatically flip the card to show the English translation
    after 3 seconds.
    Modifies:
        - global `current_card`: stores the currently displayed word pair.
        - global `timer`: stores the ID of the scheduled flip event.
    """

    global current_card, timer
    flash_card_window.after_cancel(timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_img)
    timer = flash_card_window.after(ms=3000, func=flip_card)


def is_known():
    """
    Handles the event when the user knows the current word.

    Removes the current word from the `to_learn` list, updates the
    `words_to_learn.csv` file to persist the updated list, and then
    calls `next_card()` to display a new word.
    """
    
    to_learn.remove(current_card)
    data_to_learn = pd.DataFrame(to_learn)
    data_to_learn.to_csv("./data/words_to_learn.csv", index=False)
    
    next_card()


def flip_card():
    """
    Flips the flashcard to show the English translation of the current word.

    Updates the canvas to display the back of the card with the English word
    and changes the text color to white for better contrast.
    """
    
    canvas.itemconfig(canvas_image, image=back_card_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    

# ---------------------------- UI SETUP ------------------------------- #
# Configure the window
flash_card_window = Tk()
flash_card_window.title("Flashy")
flash_card_window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Automatically flip the card after 3s delay
timer = flash_card_window.after(ms=3000, func=flip_card)

# Put card front image to the window
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_img)

# Create back image card
back_card_img = PhotoImage(file="./images/card_back.png")

# Add Language and Word to the card front image
card_title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Add wrong and right button with images
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

flash_card_window.mainloop()