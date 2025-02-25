"""Script to listen to keys in keyboard and draw the lines by controlling the turtle movement
using higher order functions."""

from turtle import Turtle, Screen

# Create an instance of Turtle class
dim = Turtle()


def move_forward():
    dim.forward(10)


def move_backward():
    dim.backward(10)


def turn_left():
    dim.left(10)


def turn_right():
    dim.right(10)


def clear_screen():
    dim.clear()
    dim.penup()
    dim.home()
    dim.pendown()


screen = Screen()
# Start listening to keyboard strokes
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
