from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create Objects that are needed
paddle1 = Paddle(-450)
paddle2 = Paddle(450)
game_ball = Ball()
score_keeper = Scoreboard()

# Setup the game screen
screen = Screen()
screen.setup(width=1000, height=600)
screen.title("The Best Pong Game")
screen.bgcolor("black")
screen.tracer(0)

# listen for keys associated with moving the paddles
screen.listen()
screen.onkeypress(paddle1.go_up, "w")
screen.onkeypress(paddle1.go_down, "s")
screen.onkeypress(paddle2.go_up, "Up")
screen.onkeypress(paddle2.go_down, "Down")

rounds = 1
game_in_progress = True
while game_in_progress:
    screen.update()
    game_ball.move()
    time.sleep(0.1)

    # Detect collision with wall
    if game_ball.ycor() > 280 or game_ball.ycor() < -270:
        game_ball.reverse_y()

    # Detect collision with paddle
    if game_ball.xcor() > 430 or game_ball.xcor() < -430:
        if game_ball.distance(paddle2.pos()) < 50 or game_ball.distance(paddle1.pos()) < 50:
            if game_ball.ball_speed < 30:
                game_ball.increase_speed()
            game_ball.reverse_x()

    # Detect when right paddle misses
    if game_ball.xcor() > 500:
        rounds += 1
        score_keeper.update_score(1)
        score_keeper.display_score()
        game_ball.reset_pos()

    # Detect when left paddle misses
    elif game_ball.xcor() < -500:
        rounds += 1
        score_keeper.update_score(2)
        score_keeper.display_score()
        game_ball.reset_pos()

    if score_keeper.score1 == 5 or score_keeper.score2 == 5:
        score_keeper.game_over()
        game_in_progress = False

screen.exitonclick()
