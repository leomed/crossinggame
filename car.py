import random
import time
from turtle import Turtle,Screen
screen = Screen()

COLORS = ["red", "orange", "yellow"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class Cars:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance = random.randint(1,6)
        """With this statement , we reduce the quantity
        of cars generated,like throwing a dice
        """
        if random_chance == 2:
            new_car = Turtle("square")
            """By default any turtle is 20pxx20px"""
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            """Here be careful, it is necessary to
            give some space at the turtle at the start,so as not
            to touch a car immediately
            """
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        """It makes the cars to move"""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def next_level(self):
        """As soon as the player goes to the next level
        the speed of the cars is incremented
        """
        self.car_speed += MOVE_INCREMENT
