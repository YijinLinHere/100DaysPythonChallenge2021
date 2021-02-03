import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########

# =======================
#       first try
# =======================
'''
# tim.pen(pensize = 1, speed = 50) #not working well
tim.pensize(1)
tim.speed("fastest")

while(True):
    tim.color(random_color())
    tim.circle(100)
    tim.right(10) 
'''
# ==========================
#       code from Angela
# ===========================

tim.speed("fastest")

def drawSpirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
    
drawSpirograph(5)

t.exitonclick()

