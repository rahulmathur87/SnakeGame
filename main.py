from turtle import Screen, Turtle
import time

screen = Screen()
screen.title("My Snake Game")
screen.screensize(600, 600)
screen.bgcolor("black")
screen.tracer(0)
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
snake_body = []

for position in starting_positions:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    snake_body.append(segment)
screen.update()

game_on = True
while game_on:
    for segment in snake_body:
        segment.forward(20)
    screen.update()
    time.sleep(1)

screen.exitonclick()
