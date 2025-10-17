from turtle import Turtle


class Scoreboard:
    def __init__(self):
        pass

    def game_over(self):
        self.game_over = Turtle()
        self.game_over.hideturtle()
        self.game_over.color("white")
        self.game_over.penup()
        self.game_over.goto(0, 0)
        self.game_over.write("Game Over!", align="center", font=("Arial", 24, "normal"))
