"""Class to create Food with circle body using Turtle module."""

import random
from turtle import Turtle


class Food(Turtle):
    """
    Class to create Food with circle body using Turtle module.
    """

    def __init__(self):
        """
        Init a food body with blue color in random screen position.
        """
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """
        Place the food in random screen position.
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
