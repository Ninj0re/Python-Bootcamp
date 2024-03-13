from my_turtle import MyTurtle


class Contestant(MyTurtle):

    def __init__(self, name):
        MyTurtle.__init__(self)
        self.shape("turtle")
        self.setheading(0)
        self.name = name

