from turtle import Turtle
from random import randint


class Food:
    def __init__(self):
        self.food = Turtle("circle")
        self.food.penup()
        self.food.color("blue")
        self.food.shapesize(0.3, 0.3, 1)
        self.refresh_food()

    def refresh_food(self):
        x = randint(0, 280)
        y = randint(0, 280)
        self.food.goto(x, y)
