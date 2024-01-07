import turtle as t

tim = t.Turtle()
screen = t.Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    cur_heading = tim.heading()
    tim.setheading(cur_heading + 10)


def turn_right():
    cur_heading = tim.heading()
    tim.setheading(cur_heading - 10)


def clear():
    tim.home()
    tim.clear()


screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear)

screen.exitonclick()
