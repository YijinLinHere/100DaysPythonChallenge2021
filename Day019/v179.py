# video 179. Aaaand, we're off to the races!

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500, height = 400 )
user_bet = screen.textinput(title = "Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
is_race_on = False

for i in range(0, 6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = -70+30*i)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} tutle is the winner!")
            else:
                print(f"You've lose. The {winning_color} tutle is the winner!")
            
            # should add a break here
            # to prevent multiple turtles reach goal at the same while loop
            # and shown You've won & You've lose at the same time
            # replace line 39, 40 with line 41 
            break

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        # turtle.forward(10)

        

screen.exitonclick()