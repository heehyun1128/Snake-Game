from turtle import Turtle

ALIGNMENT = "center"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("red")
        self.penup()
        self.goto(0,380)
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.write(f"Current Score: {self.score}",align=ALIGNMENT)
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT)
        
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()