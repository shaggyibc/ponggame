from turtle import Screen, Turtle
import time
import random

START_MOVE = [10, -10, 5, -5]

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.speed("fastest")
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        self.x_move = random.choice(START_MOVE)
        self.y_move = random.choice(START_MOVE)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
