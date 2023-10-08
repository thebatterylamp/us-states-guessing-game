import turtle
from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.screensize(600, 600)
screen.title("Guess all the U.S. States!")
image = "blank_states_img.gif"
bg = Turtle()
turtle.addshape(image)
bg.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.tolist()
correct_guesses = []
missing_states = []

while len(correct_guesses) < 50:
    guess = screen.textinput(title=f"{len(correct_guesses)}/50 Correct Guesses",
                             prompt="Name a State:\nType 'Quit' to Exit and see the states").title()

    if guess in all_states:
        correct_guesses.append(guess)
        row = data[data.state == guess]
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(row.x), int(row.y))
        t.write(guess)
    elif guess == "Quit":
        for state in all_states:
            if state not in correct_guesses:
                missing_states.append(str(state))
                row = data[data.state == state]
                d = Turtle()
                d.hideturtle()
                d.pencolor("red")
                d.penup()
                d.goto(int(row.x), int(row.y))
                d.write(state)
                new_data = pd.DataFrame(missing_states)
                new_data.to_csv("missing_states.csv")
        break

screen.exitonclick()
