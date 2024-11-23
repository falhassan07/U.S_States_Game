import pandas
from turtle import Turtle, Screen 


screen = Screen()
turtle = Turtle()

image = "blank_states_img.gif"

screen.title("U.S States Game")
screen.addshape(image)
turtle.shape(image)


guessed_states = []

while len(guessed_states) < 50:
    user_ans = (screen.textinput(f"{len(guessed_states)}/50", "What's another state's name?")).title()



    states_data = pandas.read_csv("50_states.csv")
    states = states_data["state"].to_list()


    if user_ans == "Exit":

        missed_states = [state for state in states if state not in guessed_states]

        df = pandas.DataFrame(missed_states)
        df.to_csv("missed_states.csv")
        break

    if user_ans in states:
        guessed_states.append(user_ans)
        t = Turtle()
        t.penup()
        t.hideturtle()
        data = states_data[states_data["state"] == user_ans]
        x = data["x"]
        y = data["y"]
        t.goto(x.item(),y.item())
        t.write(user_ans, font=("Arial", 20, "normal"))
        



screen.mainloop()
