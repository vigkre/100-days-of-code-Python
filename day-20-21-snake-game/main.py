"""
Build a snake game with movements using Keypress.
"""

from turtle import Screen

from food import Food
from snake import Snake
from scoreboard import Scoreboard
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
# Create a food body
food = Food()
# Create a scoreboard to track the number of food snake ate
scoreboard = Scoreboard()

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

    # Detect snake collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        # Increment the scoreboard when snake collides with food
        scoreboard.increment_score()

    # Detect collision with wall
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        game_is_on = False
        scoreboard.game_over()
    
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
