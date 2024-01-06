import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.pensize(15)
tim.speed('fastest')
direction = [0, 90, 180, 270]
colour = ['cornflower blue', 'steel blue', 'dark olive green', 'medium sea green', 'chartreuse', 'pale goldenrod',
          'light salmon',
          'rosy brown',
          'goldenrod']


def generate_random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour


for _ in range(200):
    tim.color(generate_random_colour())
    tim.forward(30)
    tim.setheading(random.choice(direction))
