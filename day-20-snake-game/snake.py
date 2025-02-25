"""
Snake class provides 3 turtles with square shaped and functions to control the movement.
"""
from turtle import Turtle
from typing import List

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SNAKE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self) -> None:
        """
        Initialize 3 square shaped turtles which are together align in the axis.
        """
        self.segments: List[Turtle] = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self) -> None:
        """
        Create 3 square shaped turtles which are together align in the axis.
        """
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self) -> None:
        """
        Move the turtle within the turtle screen of setup width.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_SNAKE)
    
    def up(self) -> None:
        """
        Move the turtle up within the turtle screen of setup width.
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self) -> None:
        """
        Move the turtle down within the turtle screen of setup width.
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def right(self) -> None:
        """
        Move the turtle right within the turtle screen of setup width.
        """
        if self.head.heading() != LEFT:       
            self.head.setheading(RIGHT)
    
    def left(self) -> None:
        """
        Move the turtle left within the turtle screen of setup width.
        """
        if self.head.heading() != RIGHT:       
            self.head.setheading(LEFT)
