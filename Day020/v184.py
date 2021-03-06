# video 184. Screen Setup and Creating a Snake Body

from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Welcome to my Snake Game")

# set tracer == 0, wait for we drawing the while picture
screen.tracer(0)

start_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

# create snake
for position in start_positions:
    new_segment = Turtle(shape = "square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

screen.update()


# moving the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    # moving strategy
    # let n cube move to n-1 position
    # and let the first cube follow the key instruction/original setting
    for seg_num in range(len(segments)-1, 0, -1):
        new_x, new_y = segments [seg_num - 1].xcor(), segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    
    segments[0].forward(20)
    # segments[0].backward(20)
    
    


screen.exitonclick()