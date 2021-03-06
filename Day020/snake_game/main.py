# video 184. Screen Setup and Creating a Snake Body

import time
from turtle import Screen, Turtle

from snake import Snake

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Welcome to my Snake Game")

# set tracer == 0, wait for we drawing the while picture
screen.tracer(0)

snake = Snake()

# control part
screen.listen() 
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


# moving the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
screen.exitonclick()
