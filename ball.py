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

    # Keeps the ball moving across the screen
    def move(self):
        self.goto(self.xcor() + self.x_direction * self.ball_speed, self.ycor() + self.y_direction * self.ball_speed)

    def reverse_x(self):
        self.x_direction *= -1

    def reverse_y(self):
        self.y_direction *= -1

    # Repositions the ball at the center of the screen
    def reset_pos(self):
        self.goto(0, 0)
        self.ball_speed = 10
        self.reverse_x()

    # Increases the speed at which the ball moves
    def increase_speed(self):
        self.ball_speed += 5