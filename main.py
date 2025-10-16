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
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(snake_body) - 1, 0, -1):
        new_x = snake_body[seg_num - 1].xcor()
        new_y = snake_body[seg_num - 1].ycor()
        snake_body[seg_num].goto(new_x, new_y)
    snake_body[0].forward(20)
    snake_body[0].left(90)

screen.exitonclick()
