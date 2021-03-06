import time
from turtle import Screen

from snake import Snake
from food import Food

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Welcome to my Snake Game")

# set tracer == 0, wait for we drawing the while picture
screen.tracer(0)

snake = Snake()
food = Food()

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

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
    
screen.exitonclick()
