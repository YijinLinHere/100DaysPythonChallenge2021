# video 178. Understanding the Turtle Coordinate System

from turtle import Turtle, Screen

screen = Screen()
screen.setup(width = 500, height = 400 )
user_bat = screen.textinput(title = "Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(0, 6):
    tim = Turtle(shape = "turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x = -230, y = -70+30*i)

screen.exitonclick()