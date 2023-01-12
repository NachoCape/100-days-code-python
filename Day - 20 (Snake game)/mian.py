from time import sleep
from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=400, height=400)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

dont_lose = True
while dont_lose:
    screen.update()
    sleep(0.08)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.grew_up()
        scoreboard.increase_score()

    if snake.head.xcor() > 190 or snake.head.xcor() < -190\
        or snake.head.ycor() > 190 or snake.head.ycor() < -190:
        dont_lose = False
        scoreboard.game_over()
    
    for i in snake.pro_snake[1:]:
        if snake.head.distance(i) < 5:
            dont_lose = False
            scoreboard.game_over()


    


screen.exitonclick()

