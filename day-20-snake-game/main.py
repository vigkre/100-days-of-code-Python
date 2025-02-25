"""
Build a snake game with movements using Keypress.
"""
from turtle import Screen
from snake import Snake
import time

# Set the game screen with title and black bg color
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game.")
# Turns turtle animation on/off and set delay for update drawings.
screen.tracer(0)

# Create snake body with 3 turtles with square shaped
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# Move the snake
game_is_on = True
while game_is_on:
    # Perform a TurtleScreen update
    screen.update()
    time.sleep(0.1)
    
    # Move the turtle within the turtle screen of setup width.
    snake.move()

screen.exitonclick()
