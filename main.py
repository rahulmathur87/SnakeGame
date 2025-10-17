from turtle import Screen
from snake import Snake
import time
# Screen setup
screen = Screen()
screen.title("My Snake Game")
screen.screensize(600, 600)
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
# Movement Key Bindings
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")
screen.listen()
screen.update()

# Game loop
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
