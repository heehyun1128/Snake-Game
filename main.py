import time
from turtle import Screen
from food import Food
from score import Score
from snake import Snake

# set up screen 
screen = Screen()
screen.setup(width=800,height=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# game init
score=Score()
snake=Snake()
food=Food()

# listen for user key input
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right,"Right")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")


game_start=True
while game_start:
    screen.update()
    time.sleep(0.15)
    snake.move()
    
    # get food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend_body()
        score.increase_score()
    
    #game is over when snake head hits the boarder    
    if snake.head.xcor()>390 or snake.head.xcor()<-390 or snake.head.ycor()>390 or snake.head.ycor()<-390:
        game_start=False
        score.game_over()
    
    for body in snake.body:
        if body==snake.head:
            pass
        # if snake head touches the body then game is over
        elif snake.head.distance(body)<10:
            game_start=False
            score.game_over()
        

screen.exitonclick()

