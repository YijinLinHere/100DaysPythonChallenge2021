import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########
tim.shape("turtle")
tim.color("red")

for _ in range(0,10):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)

t.exitonclick()