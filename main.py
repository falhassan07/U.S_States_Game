import pandas
from turtle import Turtle, Screen 


screen = Screen()
turtle = Turtle()

image = "blank_states_img.gif"

screen.title("U.S States Game")
screen.addshape(image)
turtle.shape(image)


user_ans = screen.textinput("Guess the state", "What's another state's name?")




screen.mainloop()