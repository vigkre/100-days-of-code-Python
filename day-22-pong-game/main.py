"""
Build a pong game with movements using Keypress.
"""
import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard


# 1. Create the screen for the game 
# Set the game screen with title and black bg color
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
# turn off animation
screen.tracer(0)

# 2. Create and move the paddle
# 3. Create another paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# 4. Create a ball and make it to move
ball = Ball()

# 8. Create scoreboard and keep score
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.moving_speed)
    # turn the animation on when game is on
    screen.update()
    ball.move()

    # 5. Detect collision with the wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # 6. Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # 7. 1. Detect when the right paddle misses
    if ball.xcor() > 380:
        ball.reset_positions()
        scoreboard.l_point()

    # 7. 2. Detect when the right paddle misses
    if ball.xcor() < -380:
        ball.reset_positions()
        scoreboard.r_point()

screen.exitonclick()
