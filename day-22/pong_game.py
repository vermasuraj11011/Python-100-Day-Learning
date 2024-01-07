from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score_borard import ScoreBoard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = ScoreBoard()
is_game_on = True

screen.listen()
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')

while is_game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
