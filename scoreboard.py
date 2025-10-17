from turtle import Turtle

try:
    with open("highscore.txt", "r") as file:
        content = file.read()
        HIGHSCORE = int(content)
except FileNotFoundError:
    HIGHSCORE = 0


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.show_score()

    def show_score(self):
        self.write(f"Score: {self.score} | Highscore: {HIGHSCORE}", align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.hideturtle()
        self.color("red")
        self.penup()
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("Arial", 24, "normal"))
        if self.score > HIGHSCORE:
            with open("highscore.txt", "w") as score:
                score.write(f"{self.score}")
