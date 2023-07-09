from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

#creates the snake body
class Snake:

  def __init__(self):
    self.segments = []
    self.create_snake()

  def create_snake(self):
    for i in STARTING_POSITIONS:
      tim = Turtle("square")
      tim.penup()
      tim.color("white")
      tim.goto(i)
      self.segments.append(tim)

  
  def move(self):
    for i in range(len(self.segments) - 1, 0, -1):
      new_x = self.segments[i - 1].xcor()
      new_y = self.segments[i - 1].ycor()
      self.segments[i].goto(new_x, new_y)
    self.segments[0].forward(MOVE_DISTANCE)

  
  