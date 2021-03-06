from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

# instead of some numbers, give a string for better understanding
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self):

        self.segments = []        
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):

        # create snake
        for position in START_POSITIONS:
            new_segment = Turtle(shape = "square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        # moving strategy
        # let n cube move to n-1 position
        # and let the first cube follow the key instruction/original setting
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x, new_y = self.segments [seg_num - 1].xcor(), self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        
        # go forward according to current heading
        self.head.forward(MOVE_DISTANCE)
        # self.segments[0].backward(20)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
   