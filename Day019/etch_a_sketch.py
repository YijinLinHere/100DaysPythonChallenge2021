from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def moveForwards():
    tim.forward(10)

def moveBackwards():
    tim.backward(10)

def turnCClockwise():
    tim.setheading(tim.heading()+10)

def turnClockwise():
    # tim.setheading(tim.heading()-10)
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clearDrawing():
    # tim.clear() # let reset() do all the works
    tim.reset()

screen.listen()

# remember to switch to en-en input, otherwise, your can't control the turtle by key
# screen.onkey(fun = moveForwards, key = 'w')
# screen.onkey(fun = moveBackwards, key = 's')
# screen.onkey(fun = turnCClockwise, key = 'a')
# screen.onkey(fun = turnClockwise, key = 'd') 
# screen.onkey(fun = clearDrawing, key = 'c')

screen.onkeypress(fun = moveForwards, key = 'w')
screen.onkeypress(fun = moveBackwards, key = 's')
screen.onkeypress(fun = turnCClockwise, key = 'a')
# turning would have some problem with onkeypress() ???
screen.onkeypress(fun = turnClockwise, key = 'd') 
screen.onkeypress(fun = clearDrawing, key = 'c')


screen.exitonclick() 