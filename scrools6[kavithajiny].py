import turtle

from itertools import cycle
colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

def draw_circle(size, angle, shift):
  turtle.bgcolor(next(colors))
  turtle.pencolor(next(colors))
  turtle.circle(size)
  turtle.right(angle)
  turtle.forward(shift)
  draw_circle(size+15, angle+17, shift-11)
    
turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(40)
draw_circle(37, 3, 5)