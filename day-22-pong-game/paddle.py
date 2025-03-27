"""Class to create Paddle with square body using Turtle module."""

from turtle import Turtle


class Paddle(Turtle):
    """
    Class to create Paddle with square body using Turtle module.
    """

    def __init__(self, position):
        """
        Init a Paddle body.
        """
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """
        Move the paddle up.
        """
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """
        Move the paddle down.
        """
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
