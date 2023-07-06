from turtle import Turtle, Screen
import time

#screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)

#list of snakes positions
turtle_position = [(0, 0), (-20, 0), (-40, 0)]
new_obj = []

#creates the snake body
for i in turtle_position:
  tim = Turtle("square")
  tim.penup()
  tim.color("white")
  tim.goto(i)
  new_obj.append(tim)

#moves the snake
run = True
while run:
  screen.update()
  time.sleep(0.1)
  for i in range(len(new_obj) - 1, 0, -1):
    new_x = new_obj[i - 1].xcor()
    new_y = new_obj[i - 1].ycor()
    new_obj[i].goto(new_x, new_y)
  new_obj[0].forward(20)

#screen.exitonclick()
