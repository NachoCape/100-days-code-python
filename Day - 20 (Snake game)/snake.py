from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):

    def __init__(self):
        self.pro_snake = []
        self.create_snake()
        self.head = self.pro_snake[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            original_name = Turtle("square")
            original_name.color("white")
            original_name.penup()
            original_name.goto(pos)
            self.pro_snake.append(original_name)

    def move(self):
        for square in range(len(self.pro_snake) - 1, 0, -1 ):
            new_x = self.pro_snake[square - 1].xcor()
            new_y = self.pro_snake[square - 1].ycor()
            self.pro_snake[square].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grew_up(self):
        new_quare = Turtle("square")
        new_quare.color("white")
        new_quare.penup()
        new_quare.goto(self.pro_snake[-1].position())
        self.pro_snake.append(new_quare)