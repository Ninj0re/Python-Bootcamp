import turtle
from turtle import Turtle, Screen
import random


class MyTurtle(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape("turtle")
        turtle.colormode(255)

    @staticmethod
    def __random_color():
        rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        return rgb

    def draw_square(self, width_of_square):
        for _ in range(4):
            self.forward(width_of_square)
            self.right(90)

    def draw_shapes(self, width_of_shape):

        for i in range(3, 11):
            self.pencolor(MyTurtle.__random_color())
            for _ in range(i):
                self.forward(width_of_shape)
                self.right(360/i)
        self.pencolor("black")

    def random_walk(self):
        self.speed(20)
        self.pensize(15)

        for _ in range(100):
            self.pencolor(MyTurtle.__random_color())
            direction = random.randint(0, 2) * 90
            if direction == 180:
                direction = 270

            self.__step(direction, 30)

        self.pencolor("black")
        self.speed(1)
        self.pensize(1)

    def __step(self, right_angle, length):
        self.right(right_angle)
        self.forward(length)

    def spirograph(self):
        self.speed(300)

        self.pensize(1)
        for i in range(180):
            self.pencolor(MyTurtle.__random_color())
            self.circle(180)
            self.right(2)
