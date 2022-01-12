from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xcor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.color("white")
        self.seth(90)
        self.pu()
        self.goto(xcor, 0)

    def go_up(self):
        if self.ycor() <= 220:
            self.fd(20)

    def go_down(self):
        if self.ycor() >= -220:
            self.bk(20)
