from turtle import Screen, Turtle

screen = Screen()
screen.title("My Snake Game")
screen.screensize(600, 600)
screen.bgcolor("black")
screen.tracer(0)
starting_positions = [(0, 0), (-20, 0), (-40, 0)]


for position in starting_positions:
    segment = Turtle("square")
    segment.color("white")
    segment.goto(position)
screen.update()

screen.exitonclick()
