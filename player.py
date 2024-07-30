from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.speed("fastest")
        self.setheading(90)

    def move(self):
        self.level_finish()
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def level_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            print(f"Level Up!")
            return True
        else:
            return False
