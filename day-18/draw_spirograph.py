import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def generate_random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour


tim.speed('fastest')


def draw_spirograph(gap):
    for _ in range(int(360 / gap)):
        tim.color(generate_random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
