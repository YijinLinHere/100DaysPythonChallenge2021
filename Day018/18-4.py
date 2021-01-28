import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = ["forward", "backward", "rightSide", "leftSide"]


while(True):
    color = random.choice(colours)
    direction = random.choice(directions)

    tim.pen(pensize = 5, pencolor = color, speed = 5)

    if direction == "forward":
        tim.forward(10)
    
    elif direction == "backward":
        tim.right(180)
        tim.forward(10)
    
    elif direction == "rightSide":
        tim.right(90)
        tim.forward(10)

    elif direction == "leftSide":
        tim.left(90)
        tim.forward(10)




t.exitonclick()
