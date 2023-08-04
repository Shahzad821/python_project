from turtle import Turtle
SET_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_FORWARD=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for position in SET_POSITION:
            self.add_segment(position)
           
    def add_segment(self,position):
        segment_1=Turtle("square")
        segment_1.color("white")
        segment_1.penup()
        segment_1.goto(position)
        self.segments.append(segment_1)
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for new_seg in range(len(self.segments)-1,0,-1): 
            x_seg=self.segments[new_seg-1].xcor()
            y_seg=self.segments[new_seg-1].ycor()
            self.segments[new_seg].goto(x_seg,y_seg)
        self.head.forward(MOVE_FORWARD)
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(90)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(270)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(180)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(0)
        
        


     