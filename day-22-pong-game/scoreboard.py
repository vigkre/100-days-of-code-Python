"""
Scoreboard for the arcade pong game.
"""
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    """Class to create scoreboard."""

    def __init__(self):
        """
        Init white color scoreboard on the top of the screen.
        """
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        """
        Clear the score and update scoreboard with new score.
        """
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        """
        Increment the score by 1 for left paddle and update the scoreboard.
        """
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """
        Increment the score by 1 for right paddle and update the scoreboard.
        """
        self.r_score += 1
        self.update_scoreboard()
