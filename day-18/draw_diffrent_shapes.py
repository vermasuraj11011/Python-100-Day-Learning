import random
import turtle as t

tim = t.Turtle()


def draw_shape(side):
    for _ in range(side):
        angle = 360 / side
        tim.forward(100)
        tim.right(angle)


colour = ['cornflower blue', 'steel blue', 'dark olive green', 'medium sea green', 'chartreuse', 'pale goldenrod',
          'light salmon',
          'rosy brown',
          'goldenrod']

for i in range(4, 10):
    color_choice = random.choice(colour)
    print(f'{i} -> {color_choice}')
    tim.color(color_choice)
    draw_shape(i)
