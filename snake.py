from turtle import Turtle


class Snake:
    def __init__(self):
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.snake_body = []
        for position in starting_positions:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.snake_body.append(segment)

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.snake_body[0].forward(20)

    def turn_left(self):
        self.snake_body[0].left(90)