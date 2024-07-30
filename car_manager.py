from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


def get_random_color():
    return random.choice(COLORS)


class CarManager:
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if self.car_timer() == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.speed(0)
            new_car.color(get_random_color())
            new_car.shapesize(stretch_len=2)
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(280, random.randint(-250, 250))
            self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            car.forward(self.car_speed)
            if car.xcor() < -350:
                car.clear()
                self.car_list.remove(car)

    def car_timer(self):
        return random.randint(1, 6)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
        print(f"Speed now: {self.car_speed}")
