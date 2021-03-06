# 196. Set up the Main Screen
# 197. Create a Paddle that responds to Key Presses

from turtle import Screen, Turtle


screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong")

# set tracer == 0
# wait for we drawing the canvas and show the final screen only
# it should put before create paddle
screen.tracer(0)

paddle = Turtle()
paddle.penup()
paddle.shape("square")
paddle.color("white")
paddle.resizemode("user")
paddle.shapesize(stretch_wid=5, stretch_len=1)  # each turtle squarestart with size 20*20
paddle.goto(350, 0)



def goUp():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def goDown():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(goUp, "Up")
screen.onkey(goDown, "Down")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
