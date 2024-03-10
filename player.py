from turtle import Turtle
import time


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.left(90)
        # self.color('white')
        self.penup()
        self.goto(0, -250)

    def up(self):
        self.forward(10)

    def down(self):
        self.backward(10)

    def restart(self):
        # self.hideturtle()
        self.goto(0, -250)