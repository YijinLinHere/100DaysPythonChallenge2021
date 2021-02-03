import colorgram
import turtle as t
import random

# not sure why I can't just use .\image.jpg
'''
colors = colorgram.extract('.\TheHirstPaintingProject\image.jpg', 30)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

print(rgb_colors)
'''
# color_list from image
color_list = [(248, 203, 63), (223, 169, 70), (146, 84, 37), (73, 37, 12), (240, 218, 187), (193, 140, 46), (118, 45, 19), (242, 230, 236), (95, 68, 19), (123, 186, 210), (26, 49, 21), (222, 95, 50), (76, 115, 68), (148, 175, 160), (44, 82, 35), (235, 232, 244), (102, 144, 123), (25, 15, 18), (89, 146, 153), (203, 217, 200), (142, 204, 230), (179, 207, 165), (239, 181, 147), (82, 131, 138), (122, 72, 75), (20, 20, 23), (189, 169, 174), (207, 51, 52), (143, 201, 241), (205, 185, 194)]

# color_list from image2
# color_list = [(207, 158, 116), (247, 215, 191), (141, 86, 58), (191, 233, 237), (67, 116, 66), (130, 184, 160), (185, 232, 230), (154, 215, 207), (61, 38, 29), (236, 196, 127), (24, 52, 41), (147, 215, 221), (209, 92, 67), (143, 181, 194), (246, 219, 224), (93, 154, 101), (39, 84, 48), (239, 174, 155), (61, 105, 117), (106, 48, 32), (143, 139, 88), (247, 53, 56), (180, 165, 173), (48, 35, 39), (34, 48, 56), (222, 176, 185), (72, 70, 43), (118, 81, 87), (33, 81, 84), (182, 183, 211)]

def getRandomColor():
    return random.choice(color_list)

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.setpos(-250,-250)

for row_index in range(0,10):
    tim.setheading(0)

    for column_index in range(0, 10):
        tim.dot(20, getRandomColor())
        tim.fd(50)
        
    tim.setheading(90)
    tim.fd(50)
    tim.setheading(180)
    tim.fd(500)

# ===============================
#  // another kind of for loop //
#  apply % == 0 as newline event
# ===============================
'''
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)
'''

t.exitonclick()