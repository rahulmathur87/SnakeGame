from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time

# Screen setup
screen = Screen()
screen.title("My Snake Game")
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

# Importing objects
snake = Snake()
scoreboard = Scoreboard()
food = Food()

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
    # Checking if snake eats food
    if snake.snake_body[0].distance(food) < 15:
        food.refresh_food()
        snake.grow()
        scoreboard.increase_score()
    # Checking for collision with walls
    game_on = snake.collision_checker()
    # Checking for body collision
    for segment in snake.snake_body[1:]:
        if snake.snake_body[0].distance(segment) < 10:
            game_on = False

scoreboard.game_over()
screen.exitonclick()
