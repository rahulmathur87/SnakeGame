from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.title("My Snake Game")
screen.screensize(600, 600)
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
screen.update()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
