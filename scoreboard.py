from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.ht()
        self.pu()
        self.color("white")
        self.goto(0, 190)
        self.display_score()

    # Displays the current score for both players
    def display_score(self):
        self.clear()
        self.write(f"{self.score1} {self.score2}", font=("Courier", 80, "bold"), align="center")

    def update_score(self, player):
        if player == 1:
            self.score1 += 1
        else:
            self.score2 += 1

    # Displays Game Over on the screen and stops the game
    def game_over(self):
        self.goto(0, 0)
        if self.score1 > self.score2:
            self.write("Player 1 Wins", font=("Times", 30, "bold"), align="center")
        else:
            self.write("Player 2 Wins", font=("Times", 30, "bold"), align="center")