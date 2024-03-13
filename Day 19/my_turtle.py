import turtle
from turtle import Turtle, Screen
import random


class MyTurtle(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        turtle.colormode(255)

    @staticmethod
    def random_color():
        rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        return rgb

    def event_listener(self):
        screen = Screen()
        screen.listen()
        screen.onkey(key="w", fun=self.move_forwards)
        screen.onkey(key="s", fun=self.move_backwards)
        screen.onkey(key="a", fun=self.look_left)
        screen.onkey(key="d", fun=self.look_right)
        screen.onkey(key="c", fun=screen.reset)

    def move_forwards(self):
        self.forward(10)

    def move_backwards(self):
        self.backward(10)

    def look_left(self):
        self.setheading(self.heading() + 10)

    def look_right(self):
        self.setheading(self.heading() - 10)
