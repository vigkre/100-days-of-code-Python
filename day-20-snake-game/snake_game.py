from turtle import Turtle, Screen
from typing import List
import time

# Set the game screen with title and black bg color
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game.")
# Turns turtle animation on/off and set delay for update drawings.
screen.tracer(0)

# Create snake body with 3 turtles with square shaped
segments: List[Turtle] = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

# Move the snake
game_is_on = True
while game_is_on:
    # Perform a TurtleScreen update
    screen.update()
    time.sleep(0.1)
    
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)

screen.exitonclick()
