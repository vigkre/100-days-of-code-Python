import random
import turtle as t
from turtle import Screen

colors = [
    "light blue",
    "dark green", 
    "dark turquoise",
    "dark salmon",
    "brown",
]

my_turtle = t.Turtle()
my_turtle.penup()
my_turtle.hideturtle()
# Tilt the turtle to 225 to point to west direction
my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)
my_turtle.speed("fastest")
my_turtle.showturtle()
for dot_count in range(1, 101):    
    my_turtle.dot(20, random.choice(colors))    
    my_turtle.forward(50)

    if dot_count % 10 == 0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)

screen = Screen()
screen.exitonclick()