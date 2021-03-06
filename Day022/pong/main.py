# 196. Set up the Main Screen
# 197. Create a Paddle that responds to Key Presses
# 198. Write the Paddle Class and Create the Second Paddle


from turtle import Screen
from paddle import Paddle


screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong")

# set tracer == 0
# wait for we drawing the canvas and show the final screen only
# it should put before create paddle
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


screen.listen()
screen.onkey(r_paddle.goUp, "Up")
screen.onkey(r_paddle.goDown, "Down")
screen.onkey(l_paddle.goUp, "w")
screen.onkey(l_paddle.goDown, "s")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
