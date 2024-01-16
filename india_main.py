from turtle import Turtle, Screen
import pandas

tim = Turtle()
tim.color("red")
tim.pensize(5)
tim.hideturtle()
screen = Screen()
screen.title("Indian State Game")
screen.setup(700, 800)
screen.bgpic("india_map_new.gif")

data = pandas.read_csv("indian_states_coordinates.csv")
STATE_LIST = data["states"].to_list()
TOTAL_STATE = len(STATE_LIST)

# print(STATE_LIST)
correct_ans = []
while len(correct_ans) < TOTAL_STATE:
    answer_state = screen.textinput(title=f"{len(correct_ans)}/{TOTAL_STATE} States correct",
                                    prompt="what's another state name? type 'exit' to close.").title()
    if answer_state == "Exit":
        print(correct_ans)
        not_guessed_state = []
        for state in STATE_LIST:
            if state not in correct_ans:
                not_guessed_state.append(state)
        # print(not_guessed_state)
        # print(len(not_guessed_state))
        missing_states = pandas.DataFrame(not_guessed_state)
        missing_states.to_csv("indian_states_you_missed.csv")
        break
    if answer_state in STATE_LIST:

        state_index = STATE_LIST.index(answer_state)
        state_name = (data[data.states == answer_state])
        correct_ans.append(state_name.states[state_index])
        # print(state_name)
        x_cor = float(state_name.x)
        y_cor = float(state_name.y)
        tim.penup()
        tim.goto(x_cor, y_cor)
        tim.pendown()
        tim.write(state_name.states[state_index])


# screen.exitonclick()
