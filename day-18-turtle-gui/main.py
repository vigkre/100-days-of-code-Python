import random
import turtle as t
from turtle import Screen

my_turtle = t.Turtle()
turtle_colors = [
    "light blue",
    "dark green", 
    "dark turquoise",
    "dark salmon",
    "brown",
]
directions = [0, 90, 180, 270]
t.colormode(255)

# Generate random colors as tuple
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Draw a spirograph
my_turtle.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        my_turtle.color(random_color())
        my_turtle.circle(120)
        my_turtle.setheading(my_turtle.heading() + size_of_gap)

draw_spirograph(5)


# Generate a random walk of turtle with diff colors
# my_turtle.speed("fastest")
# my_turtle.width(10)

# for _ in range(200):
#     my_turtle.color(random_color())
#     my_turtle.setheading(random.choice(directions))
#     my_turtle.forward(30)

# # Draw Different shapes starting from triangle to decagon

# my_turtle.penup()
# my_turtle.forward(100)
# my_turtle.pendown()

# shape_dim = 3
# while shape_dim < 11:
#     angle = 360/shape_dim
#     for _ in range(shape_dim):
#         my_turtle.right(angle)
#         my_turtle.forward(100)
#     shape_dim += 1


## Draw a dashed line

# for _ in range(10):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()

screen = Screen()
screen.exitonclick()
