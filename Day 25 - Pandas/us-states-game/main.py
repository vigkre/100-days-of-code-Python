import turtle
import pandas


# Create a turtle screen with game title
us_states_game_screen = turtle.Screen()
us_states_game_screen.title("U.S. States Game")

# Add image as a shape to the turtle screen
image = "blank_states_img.gif"
us_states_game_screen.addshape(image)

turtle.shape(image)

# Read data from csv file and create a list of states
states_data = pandas.read_csv("50_states.csv")
state_names = states_data.state.to_list()

correct_guesses = []

while len(correct_guesses) < 50:
    guessed_state = us_states_game_screen.textinput(
        title=f'{len(correct_guesses)}/50 states correct',
        prompt="What's the state name?"
    ).title()
    
    # Add missed states to the csv file 
    # Keep the screen until user cancel or exit
    if guessed_state == "Exit":
        missed_states = []
        for state in state_names:
            if state not in correct_guesses:
                missed_states.append(state)
        missing_state_csv = pandas.DataFrame(missed_states)
        missing_state_csv.to_csv("states_to_learn.csv")
        break   

    if guessed_state in state_names:
        turtle_obj = turtle.Turtle()
        turtle_obj.hideturtle()
        turtle_obj.penup()
        state = states_data[states_data.state == guessed_state]
        turtle.goto(int(state.x.item()), int(state.y.item()))
        turtle.write(guessed_state)
        correct_guesses.append(guessed_state)

