from turtle import Turtle, Screen 

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("My Snake game")


turtle_position = [(0, 0),(-20, 0),(-40, 0)]
new_obj = []

for i in turtle_position:
  tim = Turtle("square")
  tim.color("white")
  tim.goto(i)
  new_obj.append(tim)













screen.exitonclick()