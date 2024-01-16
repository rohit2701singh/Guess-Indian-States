from turtle import Turtle, Screen
import pandas
data = pandas.read_csv("indian_states_coordinates.csv")

tim = Turtle()
tim.speed(2)

screen = Screen()
screen.title("Indian State Game")
screen.setup(700, 825)  # hit and trial method
screen.bgpic("india_map_new.gif")
state_list = data.states.to_list()
x_cor = data.x.to_list()
y_cor = data.y.to_list()

for i in range(len(state_list)):
    # tim.penup()
    tim.pensize(2)
    tim.color("red")
    tim.goto(x_cor[i], y_cor[i])
    tim.color("black")
    tim.write(state_list[i], font=("arial", 10, "bold"))
    tim.pendown()

screen.exitonclick()
