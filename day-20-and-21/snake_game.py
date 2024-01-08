from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score_borard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extent()
        scoreboard.increase_score()

    # collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # is_game_on = False
        scoreboard.reset()
        snake.reset()
        # scoreboard.game_over()

    # collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # is_game_on = False
            scoreboard.reset()
            snake.reset()
            # scoreboard.game_over()

screen.exitonclick()
