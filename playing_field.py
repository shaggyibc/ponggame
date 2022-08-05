from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')


class Walls(Turtle):

    def __init__(self):
        super().__init__()
        self.create_wall()
        # self.upper_wall()
        # self.lower_wall()

    def create_wall(self):
        self.shape("square")
        # self.hideturtle()
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=70, stretch_wid=1)
        self.speed("fastest")



