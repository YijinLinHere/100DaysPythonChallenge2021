import time
from turtle import Screen

from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Welcome to my Snake Game")

# set tracer == 0, wait for we drawing the while picture
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

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
        snake.extend()
        scoreboard.addon()
    
    # Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.showGameOver()
        game_is_on = False

    # Destect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            # since the distance between head and head is < 10
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.showGameOver
    
screen.exitonclick()
