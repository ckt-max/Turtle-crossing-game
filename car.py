from turtle import Turtle
import time
import random

class Car(Turtle):

    def __init__(self):
        super().__init__()
        colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
        self.hideturtle()
        self.penup()
        self.shape('square')
        self.color(random.choice(colors))
        self.shapesize(2, 4)
        self.goto(400, random.randrange(-200, 250, 30))
        self.showturtle()


        # for i in range(self.n):
        #     new_car = Turtle(shape = 'square')
        #     new_car.hideturtle()
        #     new_car.color(random.choice(self.car_list))
        #     new_car.penup()
        #     new_car.goto(800, random.randrange(-250,250,1))
        #     new_car.showturtle()

    def move(self,level):
        self.back(0.1*level)



