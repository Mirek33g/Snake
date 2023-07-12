from turtle import Screen
from snake import Snake
import time
from food import Food

#screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)

snake = Snake()
food = Food()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#moves the snake
run = True
while run:
  screen.update()
  time.sleep(0.1)
  snake.move()

  #detect the colision with food
  if snake.head.distance(food) < 15:
    food.refresh()




#screen.exitonclick()
