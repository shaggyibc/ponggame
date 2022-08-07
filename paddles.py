from turtle import Turtle

POSITION = [(640, 0), (-640, 0)]


class Paddles(Turtle):

    def __init__(self):
        super().__init__()
        self.paddles = []
        self.paddle_setup()
        self.left_paddle = self.paddles[1]
        self.right_paddle = self.paddles[0]

    def paddle_setup(self):
        for positions in POSITION:
            self.create_paddles(positions)

    def create_paddles(self, positions):
        new_paddle = Turtle()
        new_paddle.shape("square")
        new_paddle.color("white")
        new_paddle.penup()
        new_paddle.shapesize(stretch_len=5, stretch_wid=1)
        new_paddle.speed("fastest")
        new_paddle.goto(positions)
        new_paddle.setheading(90)
        self.paddles.append(new_paddle)

    def up_right(self):
        self.right_paddle.setheading(90)
        self.right_paddle.forward(60)

    def down_right(self):
        self.right_paddle.setheading(270)
        self.right_paddle.forward(60)

    def up_left(self):
        self.left_paddle.setheading(90)
        self.left_paddle.forward(60)

    def down_left(self):
        self.left_paddle.setheading(270)
        self.left_paddle.forward(60)
