# 190. Create a Scoreboard and Keep Score
from turtle import Turtle

# seperate parameter and code
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        
        self.shape("classic")
        self.goto(0, 270)
        self.color("white") # change the color before write()
        self.hideturtle() # let turtle icon gone!

        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.write("Score: {}".format(self.score), align = ALIGNMENT, font = FONT)
    
    def showGameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = ALIGNMENT, font = FONT)

    def addon(self):
        self.score += 1
        self.clear()
        self.updateScoreBoard()
        


