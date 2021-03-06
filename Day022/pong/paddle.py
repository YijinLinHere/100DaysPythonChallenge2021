# 198. Write the Paddle Class and Create the Second Paddle

from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, xy_tuple):
        super().__init__()
    
        self.penup()
        self.shape("square")
        self.color("white")
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)  # each turtle squarestart with size 20*20
        self.goto(xy_tuple[0], xy_tuple[1])

    def goUp(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def goDown(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)