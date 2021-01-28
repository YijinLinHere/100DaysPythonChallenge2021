import turtle as t
import random

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

'''
# before refactor
tim.shape("turtle")

target_shape = [4, 5, 6, 7, 8, 9, 10]
for shape_n in target_shape:
    
    t.colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.pencolor(r, g, b)

    turning_angle = 360/shape_n

    for _ in range(0, shape_n):
        tim.forward(100)
        tim.right(turning_angle)
t.exitonclick()
'''

def random_pick_color():
    t.colormode(255)
    
    # simple one, but won't have 100, 100, 100 serquence
    r, g, b = random.sample(range(0, 255), 3)
    tim.pencolor(r, g, b)


def draw_shape(num_sides):
    turning_angle = 360/num_sides

    for _ in range(0, num_sides):
        tim.forward(100)
        tim.right(turning_angle)


if __name__ == "__main__":
    for shape_side_n in range(3, 11):
        random_pick_color()
        draw_shape(shape_side_n)


t.exitonclick()
