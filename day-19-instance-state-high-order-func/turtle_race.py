"""Script to create a turtle race game with 6 turtles."""

import random
from turtle import Turtle, Screen
from typing import List

# Create a screen with required width and height
screen = Screen()
screen.setup(width=500, height=400)

# Prompt the user to get their preferred winner
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)

colors = ["red", "green", "blue", "yellow", "orange", "purple"]
contestants: List[Turtle] = []
y_coord = -60
is_race_on = False


# Create contestant for the race with different states like color, coordinates
def create_contestant(color: str, y_coord: int):
    turt = Turtle(shape="turtle")
    turt.color(color)
    turt.penup()
    turt.goto(x=-230, y=y_coord)
    return turt


for color in colors:
    contestants.append(create_contestant(color=color, y_coord=y_coord))
    y_coord += 30


# Start the race when the user has provided the bet
if user_bet:
    is_race_on = True

while is_race_on:
    for contestant in contestants:
        if contestant.xcor() > 230:
            winning_color = contestant.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! {winning_color} is the winner")
            else:
                print(f"You've lost! {winning_color} is the winner")
        rand_distance = random.randint(0, 10)
        contestant.forward(rand_distance)

screen.exitonclick()
