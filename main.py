from turtle import Screen
from snake import Snake
import time

#screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)

snake = Snake()

#moves the snake
run = True
while run:
  screen.update()
  time.sleep(0.1)
  snake.move()

#screen.exitonclick()
