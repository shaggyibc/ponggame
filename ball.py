from turtle import Screen, Turtle
import time


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
        self.left(45)

    def bounce(self):
        angle = self.heading()
        self.setheading(angle + 90)
