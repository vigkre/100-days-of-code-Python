"""https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203
    &url=worlds%2Tutorial_en%2Fhurdle3.json"""


# Hurdles race
# Reeborg has entered a hurdle race. Make him run the course, following the path shown.
# The position and number of hurdles changes each time this world is reloaded.
# What you need to know
# The functions move() and turn_left().
# The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
# How to use a while loop and an if statement.
# Your program should also be valid for worlds Hurdles 1 and Hurdles 2.

# My Solution

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def immediate_wall_jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
#
# while not at_goal():
#     if wall_in_front():
#         immediate_wall_jump()
#     elif front_is_clear():
#         move()

# Solution from course

# while not at_goal():
#     if wall_in_front():
#         immediate_wall_jump()
#     else:
#         move()
