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

    def collision_checker(self):
        if self.snake_body[0].xcor() >= 290 or self.snake_body[0].xcor() <= -290:
            return False
        elif self.snake_body[0].ycor() >= 290 or self.snake_body[0].ycor() <= -290:
            return False
        else:
            return True

    def go_up(self):
        if int(self.snake_body[0].heading()) != 270:
            self.snake_body[0].setheading(90)

    def go_down(self):
        if int(self.snake_body[0].heading()) != 90:
            self.snake_body[0].setheading(270)

    def go_left(self):
        if int(self.snake_body[0].heading()) != 0:
            self.snake_body[0].setheading(180)

    def go_right(self):
        if int(self.snake_body[0].heading()) != 180:
            self.snake_body[0].setheading(0)
