"""Class to create ball with circle body using Turtle module."""

from turtle import Turtle

class Ball(Turtle):
    """
    Class to create ball with circle body using Turtle module.
    """

    def __init__(self):
        """
        Init a ball body with white color in (0,0) screen position.
        """
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.moving_speed = 0.1

    def move(self):
        """
        Move the ball in the direction calculated.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Bounce when hitting the right paddle.
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Bounce when hitting the left paddle.
        """
        self.x_move *= -1
        self.moving_speed *= 0.9
    
    def reset_positions(self):
        """
        Bring back the ball to home position and move in opp paddle direction.
        """
        self.home()        
        self.moving_speed = 0.1
        self.bounce_x()
