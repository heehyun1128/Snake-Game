from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    
    def __init__(self):
        self.body=[]
        self.create_snake()
        self.head=self.body[0]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_body_part(position)
            
    def add_body_part(self,position):
        new_body=Turtle("square")
        new_body.color("white")
        new_body.penup()
        new_body.goto(position)
        
        self.body.append(new_body)
    
    def extend_body(self):
        self.add_body_part(self.body[-1].position())
        
# get the new coordinate of the snake
    def move(self):
        for body_position in range(len(self.body)-1,0,-1):
            updated_xcor = self.body[body_position-1].xcor()
            updated_ycor =self.body[body_position-1].ycor()
            self.body[body_position].goto(updated_xcor,updated_ycor)
        # move head to the new position
        self.head.forward(MOVE_DISTANCE)
        
    
    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)
            
    def down(self):
        if self.head.heading() !=UP:
            self.head.setheading(DOWN)
            
    def left(self):
        if self.head.heading() !=RIGHT:
            self.head.setheading(LEFT)
            
    def right(self):
        if self.head.heading() !=LEFT:
            self.head.setheading(RIGHT)