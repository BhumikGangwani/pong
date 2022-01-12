from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_direction = 1
        self.y_direction = 1
        self.ball_speed = 10
        self.shape("square")
        self.color("white")
        self.pu()

    def move(self):
        self.goto(self.xcor() + self.x_direction * self.ball_speed, self.ycor() + self.y_direction * self.ball_speed)

    def reverse_x(self):
        self.x_direction *= -1

    def reverse_y(self):
        self.y_direction *= -1

    def reset_pos(self):
        self.goto(0, 0)
        self.ball_speed = 10
        self.reverse_x()

    def increase_speed(self):
        self.ball_speed += 5