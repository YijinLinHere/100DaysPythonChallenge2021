import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

'''
# ---------------------------------------------
#              before refactor
# ---------------------------------------------

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
'''

# ---------------------------------------------
#              after refactor
# ---------------------------------------------
t.colormode(255)

def getRandomColor():
    r = random.randint(0, 255)  
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

directions = [0, 90, 180, 270]
tim.pen(pensize = 15, speed = 10)
# tim.speed("fastest")
# tim.pensize(15)

while(True):
    # tim.color(random.choice(colours))
    tim.color(getRandomColor())
    tim.forward(30)
    tim.setheading(random.choice(directions))



t.exitonclick()
