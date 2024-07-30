from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.level = 1
        self.level_pen = Turtle()
        self.level_pen.speed(0)
        self.level_pen.color("black")
        self.level_pen.penup()
        self.level_pen.goto(0, 250)
        self.level_pen.hideturtle()
        self.update_level()

    def update_level(self):
        self.level_pen.clear()
        self.level_pen.write(f"Level: {self.level}", font=FONT, align="center")

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.level_pen.clear()
        self.level_pen.goto(0, 0)
        self.level_pen.write(f"Game Over!", font=FONT, align="center")

