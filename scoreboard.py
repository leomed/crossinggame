from turtle import Turtle,Screen
screen = Screen()

FONT = ('Lucida Console', 10)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(-250,270)
        self.color("Black")
        self.write(f"Score : {self.score}", align="center", font=FONT)

    def increment_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)

