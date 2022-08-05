from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=40, stretch_wid=1)
        self.speed("fastest")
        self.goto(0, 340)
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.right_score}    Score   {self.left_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.left_score += 1
        self.clear()
        self.update_scoreboard()
