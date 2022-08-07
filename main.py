import turtle
from turtle import Screen, Turtle
import time
from ball import Ball
from paddles import Paddles
from playing_field import Walls
# from food import Food
from scoreboard import Scoreboard
points = 0
screen = Screen()
screen.setup(width=1.0, height=1.0)
screen.screensize(1300, 700, "black")
screen.title("Is that a ball in your pants?")
screen.tracer(0)


score = Scoreboard()
pong = Ball()
paddle = Paddles()

# paddle.left_paddle.goto(200, 0)

wall_up = Walls()
wall_up.goto(0, 380)
wall_down = Walls()
wall_down.goto(0, -315)
ball_speed = turtle.numinput(title="Game Speed", prompt="How fast do you want the ball to "
                                                        "move 1(slowest) through 100(fastest)")
screen.listen()
screen.onkey(key="Up", fun=paddle.up_right)
screen.onkey(key="Down", fun=paddle.down_right)
screen.onkey(key="a", fun=paddle.up_left)
screen.onkey(key="z", fun=paddle.down_left)

game_is_on = True

while game_is_on:
    time.sleep(.10 / ball_speed)
    screen.update()
    pong.move()
    if pong.ycor() > 370:
        pong.bounce()
    elif pong.ycor() < -305:
        pong.bounce()
    elif pong.xcor() > 650:
        # pong.bounce()
        score.increase_score_left()
        pong.hideturtle()
        pong = Ball()
    elif pong.xcor() < -650:
        score.increase_score_right()
        pong.hideturtle()
        pong = Ball()
        # pong.bounce()
    elif pong.distance(paddle.right_paddle) < 50 and pong.xcor() > 625:
        pong.paddle_bounce()
    elif pong.distance(paddle.left_paddle) < 50 and pong.xcor() < -625:
        pong.paddle_bounce()















screen.exitonclick()