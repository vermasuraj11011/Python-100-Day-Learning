import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S States Game')

image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv('50_states.csv')
states = data.state.to_list()

guess_states = []


while len(guess_states) < len(states):
    answer_state = screen.textinput(title=f'{len(guess_states)}/50 States Correct',
                                    prompt="What's another State name").title()
    if answer_state == 'Exit':
        missing_states = []
        for state in states:
            if state not in guess_states:
                missing_states.append(state)
        missed_data = pandas.DataFrame(missing_states)
        missed_data.to_csv('missed_states.csv')
        print(missing_states)
        break

    if answer_state in states:
        guess_states.append(answer_state)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state = data[data.state == answer_state]
        tim.goto(int(state.x), int(state.y))
        tim.write(answer_state)

