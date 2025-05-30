import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# 1. Create and move a turtle with a KeyPress
player = Player()

# 2. Create and move randomly generated cars
car_manager = CarManager()

# 5. Create and update scoreboard
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # 3. Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # 4. Detect when player finishes
    if player.is_on_finish_line():
        player.goto_start()
        car_manager.level_up()
        scoreboard.increment_level()


screen.exitonclick()
