import turtle
import pandas

screen = turtle.Screen()
screen.title("us_states_game")

image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
guess_states = []

while len(guess_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guess_states)}/50 guessed",
        prompt="type the state name"
    ).title()

    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guess_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("to_learn")
        break

    if answer_state in state_list and answer_state not in guess_states:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state)



