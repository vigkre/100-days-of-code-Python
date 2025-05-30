"""
Scoreboard for the Turtle crossing game.
"""

from turtle import Turtle

FONT = ("Poppins", 24, "normal")


class Scoreboard(Turtle):
    """Class to create scoreboard."""

    def __init__(self):
        """
        Init black color scoreboard on the top of the screen.
        """
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(x=-250, y=250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Clear the score and update scoreboard with new score.
        """
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        """
        Stop the game and display game over in the center.
        """
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def increment_level(self):
        """
        Increment the level by 1 and update the scoreboard.
        """
        self.level += 1
        self.update_scoreboard()
