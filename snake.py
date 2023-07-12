from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DIRECTIONS = [90, 180, 270]
UP = 90
DOWN = 279
LEFT = 180
RIGHT = 0

#creates the snake body
class Snake:

  def __init__(self):
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]

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
    self.head.forward(MOVE_DISTANCE)

  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)

  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)

  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)

  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)