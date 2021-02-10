from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def moveForwards():
    tim.forward(10)


screen.listen()

# remember to switch to en-en input, otherwise, your can't control the turtle by key
screen.onkey(fun = moveForwards, key = "space")
screen.exitonclick() 