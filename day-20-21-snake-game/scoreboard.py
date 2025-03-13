"""
Scoreboard for the snake game.
"""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Poppins", 24, "normal")


class Scoreboard(Turtle):
    """Class to create scoreboard."""

    def __init__(self):
        """
        Init white color scoreboard on the top of the screen.
        """
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Clear the score and update scoreboard with new score.
        """
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """
        Stop the game and display game over in the center.
        """
        self.goto(0, 0)
        self.write("Game Over.", align=ALIGNMENT, font=FONT)

    def increment_score(self):
        """
        Increment the score by 1 and update the scoreboard.
        """
        self.score += 1
        self.update_scoreboard()
