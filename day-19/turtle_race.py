import random
import turtle as t

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

screen = t.Screen()
screen.setup(width=500, height=400)

space = 100
turtles = []
for turtle_index in range(0, 6):
    tim = t.Turtle(shape='turtle')
    tim.color(colors[turtle_index])
    turtles.append(tim)
    tim.penup()
    tim.goto(-230, space)
    space -= 40

is_race_on = False

user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter the colour: ')
print(user_bet)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle_index in turtles:
        if turtle_index.xcor() > 230:
            is_race_on = False
            winning_color = turtle_index.pencolor()
            if user_bet == winning_color:
                print(f'You won! {winning_color} won the race')
            else:
                print(f'You lose! {winning_color} won the race')
            break
        random_dis = random.randint(0, 10)
        turtle_index.forward(random_dis)

screen.exitonclick()
